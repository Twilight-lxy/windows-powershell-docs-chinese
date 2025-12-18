---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BackgroundIntelligentTransfer.Management.dll-Help.xml
Module Name: BitsTransfer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitstransfer/start-bitstransfer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-BitsTransfer
---

# Start-BitsTransfer

## 摘要
创建一个BITS传输作业。

## 语法

```
Start-BitsTransfer [-Asynchronous] [-Dynamic] [-CustomHeadersWriteOnly] [-Authentication <String>]
 [-Credential <PSCredential>] [-Description <String>] [-HttpMethod <String>] [[-Destination] <String[]>]
 [-DisplayName <String>] [-Priority <String>] [-TransferPolicy <CostStates>] [-ACLFlags <ACLFlagValue>]
 [-SecurityFlags <SecurityFlagValue>] [-UseStoredCredential <AuthenticationTargetValue>]
 [-ProxyAuthentication <String>] [-ProxyBypass <String[]>] [-ProxyCredential <PSCredential>]
 [-ProxyList <Uri[]>] [-ProxyUsage <String>] [-RetryInterval <Int32>] [-RetryTimeout <Int32>]
 [-MaxDownloadTime <Int32>] [-Source] <String[]> [-Suspended] [-TransferType <String>]
 [-CustomHeaders <String[]>] [-NotifyFlags <NotifyFlagValue>] [-NotifyCmdLine <String[]>]
 [-CertStoreLocation <CertStoreLocationValue>] [-CertStoreName <String>] [-CertHash <Byte[]>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Start-BitsTransfer` cmdlet 用于创建一个后台智能传输服务（BITS）任务，以便在客户端计算机和服务器之间传输一个或多个文件。`TransferType` 参数用于指定传输的方向。默认情况下，在 cmdlet 开始传输后，命令提示符将处于不可用状态，直到传输完成或传输进入错误状态为止。如果返回的 `BitsJob` 对象的状态为 `Error`，则该对象中会包含错误代码和描述信息，这些信息可用于故障分析。

`Start-BitsTransfer` cmdlet 支持从服务器下载多个文件到客户端计算机，但通常不支持从客户端计算机上传多个文件到服务器。如果您需要上传多个文件，可以使用 `Import-Csv` cmdlet 将输出结果传递给 `Add-BitsFile` cmdlet 来完成上传操作。或者，您也可以考虑使用 cabinet 文件（.cab）或压缩文件（.zip）来进行文件传输。

## 示例

### 示例 1：创建一个 BITS 传输作业来下载文件
```
PS C:\> Start-BitsTransfer -Source "http://server01/servertestdir/testfile1.txt" -Destination "c:\clienttestdir\testfile1.txt"
```

该命令创建一个 BITS（Binary Transfer Service）传输任务，用于从服务器下载文件。文件的本地路径和远程路径分别由 *Source*（源）和 *Destination*（目标）参数指定。由于默认的传输类型是“下载”，因此 `http://Server01/servertestdir/testfile1.txt` 文件会被传输到客户端上的 `C:\clienttestdir\testfile1.txt`。当文件传输完成或遇到错误时，命令提示符会停止显示。

当你将文件上传到HTTP地址时，*TransferType* 参数必须设置为 **Upload**。

由于 `Start-BitsTransfer` cmdlet 在没有指定参数值时，默认认为第一个参数是源位置，第二个参数是目标位置，因此该命令可以简化如下：

`Start-BitsTransfer "http://server01/servertestdir/testfile1.txt" "c:\clienttestdir\testfile1.txt"`

### 示例 2：创建用于下载多个文件的 BITS（Binary Transfer Service）传输任务
```
PS C:\> Import-CSV filelist.txt | Start-BitsTransfer
```

此命令用于创建BITS传输任务，以便从服务器下载多个文件。

该命令会导入源文件和目标文件的路径信息，然后将这些路径信息传递给 **Start-BitsTransfer** 命令。**Start-BitsTransfer** 命令会为 `filelist.txt` 中的每个文件创建一个新的 BITS 传输任务，并同时将这些文件传输到客户端。

filelist.txt 文件的内容类似于以下信息：

源文件、目标文件：  
http://server01/servertestdir/testfile1.txt，c:\clienttestdir\testfile1.txt  
http://server01/servertestdir/testfile2.txt，c:\clienttestdir\testfile2.txt  
http://server01/servertestdir/testfile3.txt，c:\clienttestdir\testfile3.txt  
http://server01/servertestdir/testfile4.txt，c:\clienttestdir\testfile4.txt

**注意：** 文件的第一行必须包含源地址（Source）和目标地址（Destination）的标题信息，例如示例中所展示的内容。

### 示例 3：创建一个 BITS 传输任务来上传文件
```
PS C:\> Start-BitsTransfer -Source "c:\clienttestdir\testfile1.txt" -Destination "http://server01/servertestdir/testfile1.txt" -TransferType Upload
```

该命令创建了一个 BITS（Binary Transfer Service）传输任务，用于将文件上传到服务器。文件的本地路径和远程路径分别由 **Source**（源路径）和 **Destination**（目标路径）参数指定。由于默认的传输类型是“下载”（Download），因此必须将 **TransferType** 参数设置为 “Upload”（上传）。客户端上的 `C:\clienttestdir\testfile1.txt` 文件会被传输到服务器上的 `http://Server01/servertestdir/testfile1.txt`。文件传输完成后，命令提示符会返回正常状态；如果发生错误，则会显示相应的错误信息。

`Start-BitsTransfer` cmdlet 可以从服务器将多个文件下载到客户端计算机，但通常不能从客户端计算机将多个文件上传到服务器。可以通过使用 `Import-Csv` cmdlet 将输出结果传递给 `Start-BitsTransfer` cmdlet 来规避这一限制。如果需要上传多个文件，也可以使用 `.cab` 或 `.zip` 格式的文件。

由于 `Start-BitsTransfer` cmdlet 在没有指定参数值时，默认认为第一个参数是源位置，第二个参数是目标位置，因此该命令可以简化如下：

`Start-BitsTransfer "c:\clienttestdir\testfile1.txt" "http://server01/servertestdir/testfile1.txt" -TransferType Upload`

### 示例 4：创建一个 BITS 转移任务，用于下载多个文件
```
PS C:\> Start-BitsTransfer -Source "http://server01/servertestdir/testfile1.txt", "http://server01/servertestdir/testfile2.txt" -Destination "c:\clienttestdir\testfile1.txt", "c:\clienttestdir\testfile2.txt"
```

此命令创建了一个BITS传输任务，用于从服务器下载多个文件。

文件的本地名称和远程名称分别通过*Source*（源）和*Destination*（目标）参数来指定。由于*TransferType*（传输类型）参数的默认值为“Download”（下载），因此`http://Server01/servertestdir/testfile1.txt`和`http://Server01/servertestdir/testfile2.txt`这两个文件会被传输到客户端计算机上的`C:\clienttestdir\testfile1.txt`和`C:\clienttestdir\testfile2.txt`文件夹中。文件传输完成后，命令提示符会返回正常状态；如果传输过程中出现错误，则会显示相应的错误信息。

### 示例 5：创建一个 BITS 传输任务，使用特定的凭据集下载文件
```
PS C:\> $Cred = Get-Credential
PS C:\> Start-BitsTransfer -DisplayName MyJob -Credential $Cred -Source "http://server01/servertestdir/testfile1.txt" -Destination "c:\clienttestdir\testfile1.txt"
```

这个示例创建了一个BITS传输任务，该任务使用一组特定的凭据从服务器下载文件。

第一个命令通过调用 **Get-Credential** cmdlet 从用户那里获取一组凭据。返回的 **PSCredential** 对象被存储在 `$Cred` 变量中。

第二个命令使用了 *Credential* 参数，将存储在 $Cred 变量中的 **PSCredential** 对象传递给 **Start-BitsTransfer** cmdlet。这样就创建了一个新的 BITS 传输任务，该任务会将 `http://server01/servertestdir/testfile1.txt` 文件下载到客户端。指定的凭据用于在服务器上验证用户的身份。此外，可选的 *DisplayName* 参数用于为这个 BITS 传输任务指定一个唯一的名称。

### 示例 6：创建用于下载多个文件的 BITS 传输作业
```
PS C:\> Import-CSV filelist.txt | Start-BitsTransfer -Asynchronous -Priority Normal
```

该命令用于创建BITS传输作业，用于从服务器下载多个文件。这些文件是按顺序下载的，但一旦传输作业完成，它们就可以立即被使用了。

该命令会导入源文件和目标文件的路径，然后将这些信息传递给 **Start-BitsTransfer** 命令。**Start-BitsTransfer** 命令会根据 filelist.txt 文件中的每一条文件记录创建一个新的 BITS（Bit Transfer Service）传输任务，并依次将这些文件传输到客户端。

filelist.txt 文件的内容类似于以下信息：

源文件、目标文件：  
http://server01/servertestdir/testfile1.txt，c:\clienttestdir\testfile1.txt  
http://server01/servertestdir/testfile2.txt，c:\clienttestdir\testfile2.txt  
http://server01/servertestdir/testfile3.txt，c:\clienttestdir\testfile3.txt  
http://server01/servertestdir/testfile4.txt，c:\clienttestdir\testfile4.txt

**注意：** 文件的第一行必须包含源地址（Source）和目标地址（Destination）的标题信息，例如示例中所展示的内容。

### 示例 7：创建一个 BITS 传输任务以下载多个文件
```
PS C:\> Start-BitsTransfer -Source C:\clientsourcedir\*.txt -Destination c:\clientdir\ -TransferType Download
```

在上面的例子中，`Start-BitsTransfer` 命令创建了一个新的 BITS（Bit Transfer Service）传输任务。所有的文件都被添加到这个任务中，并依次传输给客户端。

> [!注意] > 目标路径不能使用通配符。目标路径支持相对目录、根目录或隐式目录（即当前目录）。无法通过使用通配符来重命名目标文件。此外，HTTP 和 HTTPS URL 也不支持通配符。通配符仅适用于 UNC 路径和本地目录。

### 示例 8：创建用于上传多个文件的 BITS（Binary Internet Transfer Service）传输任务
```
PS C:\> Import-CSV filelist.txt | Start-BitsTransfer -TransferType Upload
```

这个命令用于创建BITS传输任务，将这些文件上传到服务器上。

该命令会导入源文件和目标文件的路径信息，然后将这些信息传递给 **Start-BitsTransfer** 命令。**Start-BitsTransfer** 命令会根据 filelist.txt 中列出的每个文件创建一个新的 BITS 传输任务，并同时将这些文件传输到服务器上。

filelist.txt 文件的内容类似于以下信息：

源文件路径：  
c:\clienttestdir\testfile1.txt  
目标文件路径：  
http://server01/servertestdir/testfile1.txt  

其他源文件路径及目标文件路径相同：  
c:\clienttestdir\testfile2.txt → http://server01/servertestdir/testfile2.txt  
c:\clienttestdir\testfile3.txt → http://server01/servertestdir/testfile3.txt  
c:\clienttestdir\testfile4.txt → http://server01/servertestdir/testfile4.txt

**注意：** 文件的第一行必须包含源地址（Source）和目标地址（Destination）的标题信息，例如示例中所展示的内容。


### 示例 9：从网络中的一台服务器下载文件到另一台位于不同网络的客户端上，这两台设备通过代理服务器相互连接
```
PS C:\> Start-BitsTransfer -Source .\Patch0416.msu -Destination $env:temp\Patch0416.msu -ProxyUsage Override -ProxyList BitsProxy:8080 -ProxyCredential Server01\Admin01
```

这个命令使用 **Start-BitsTransfer** cmdlet，在两个网络仅通过代理服务器连接的情况下，将一个补丁文件从一个网络的服务器复制到另一个网络的客户端。

这种情况发生在连接到互联网的服务器下载文件后，将这些文件分发到那些未连接互联网或处于孤立状态、无法访问互联网的计算机上时。

BITS 可以自动检测代理服务器的设置。但是，如果代理服务器未配置为支持自动检测，那么您可以覆盖自动检测机制，并手动指定代理服务器的位置，如下例所示。

该命令使用 *Source* 参数来指定服务器上补丁文件的位置，使用 *Destination* 参数来指定客户端计算机上补丁文件的目标位置。它通过设置 *ProxyUsage* 参数的值为 **Override** 来覆盖自动检测代理服务器的机制；为了识别代理服务器，它使用了 *ProxyList* 参数，该参数的值是一个采用 `<Name:Port>` 格式的 URI。最后，它使用 *ProxyCredential* 参数来指定具有连接代理服务器权限的管理员的凭据信息。

## 参数

### -ACLFlags
指定传输作业的所有者和访问控制列表（ACL）信息。可以选择以下一个或多个值：

- o: Copy owner information with file.
- g: Copy group information with file.
- d: Copy discretionary access control list (DACL) information with file.
- s: Copy system access control list (SACL) information with file.

```yaml
Type: ACLFlagValue
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Asynchronous
该命令表示cmdlet会在后台创建并处理BITS传输任务。在BITS传输任务创建完成后，命令提示符会立即重新显示出来。返回的`BitsJob`对象可用于监控任务的状态和进展。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Authentication
指定在服务器上使用的认证机制。该参数的可接受值包括：

- **Basic**: Basic is a scheme in which the user name and password are sent in clear text to the server or proxy.

- **Digest**: Digest is a challenge-response scheme that uses a server-specified data string for the challenge.

- **Ntlm**: NT LAN Manager (NTLM) is a challenge-response scheme that uses the credentials of the user for authentication in a Windows-based network environment.

- **Negotiate** (the default): Negotiate is a challenge-response scheme that negotiates with the server or proxy to determine which scheme to use for authentication. For example, this parameter value allows negotiation to determine whether the Kerberos protocol or NTLM is used.

- **Passport**: Passport is a centralized authentication service provided by Microsoft that offers a single logon for member sites.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Basic, Digest, Ntlm, Negotiate, Passport

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertHash
指定一个用于识别证书的SHA1哈希值。

```yaml
Type: Byte[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertStoreLocation
指定用于查找证书的证书存储位置。有效值包括：

- CURRENT_USER
- LOCAL_MACHINE
- CURRENT_SERVICE
- SERVICES
- USERS
- CURRENT_USER_GROUP_POLICY
- LOCAL_MACHINE_GROUP_POLICY
- LOCAL_MACHINE_ENTERPRISE

```yaml
Type: CertStoreLocationValue
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertStoreName
指定证书存储的名称。有效值包括：

- CA: Certification Authority certificates
- MY: Personal certificates
- ROOT: Root certificates
- SPC: Software Publisher Certificate

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前，会提示您确认是否要继续执行该操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于向服务器进行身份验证的凭据；该服务器由*Source*参数的值所标识。默认情况下使用当前用户的信息。

请输入一个用户名，例如 “User01”、“Domain01/User01” 或 “User@Contoso.com”。或者，使用 **Get-Credential** cmdlet 来为该参数生成相应的值。在输入用户名后，系统会要求您输入密码。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CustomHeaders
指定一个或多个自定义的 HTTP 标头，这些标头将包含在发送到服务器的请求中。请提供一个字符串数组作为参数。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CustomHeadersWriteOnly
表示此作业的HTTP自定义头部仅允许写入（即不允许读取）。

当你的自定义头部包含安全信息时，请使用此参数。同一台计算机上的其他程序无法读取这些头部信息。不过，BITS进程可以读取这些头部信息，并通过HTTP连接将它们传输出去。

一旦您将某个任务的头部设置为“只读”（write-only），就无法再更改该任务的此值了。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Description
描述了BITS传输作业的相关信息。该描述的长度限制为1,024个字符。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Destination
指定一个数组，其中包含目标位置以及您想要传输的文件的名称。目标文件名与相应的源文件名成对出现。例如，*Source* 参数中指定的第一个文件名对应于 *Destination* 参数中的第一个文件名，*Source* 参数中的第二个文件名对应于 *Destination* 参数中的第二个文件名。*Source* 和 *Destination* 参数必须具有相同数量的元素；否则，该命令将产生错误。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DisplayName
为BITS传输作业指定一个显示名称。该显示名称为用户提供了一种便于区分不同BITS传输作业的方式。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Dynamic
表示转账使用了动态设置。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HttpMethod
指定一种除默认方法（GET）之外的传输方式。如果您指定了 GET 方法，该参数将无效。

如果您指定了某个方法，该任务将获得前台优先级（foreground priority），并且这个优先级无法被更改。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxDownloadTime
指定作业中传输文件的最大时间（以秒为单位）。默认值为 7,776,000 秒，即 90 天。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NotifyCmdLine
指定一个在作业完成或遇到错误后运行的程序。该程序是在运行此 cmdlet 的用户的上下文中执行的。

请将程序名称以及所有参数以字符串数组的形式提供给我。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NotifyFlags
指定您希望接收的事件通知类型，例如作业转移事件。有效值包括：

- 1: Generates an event when all files in the job have been transferred.
- 2: Generates an event when an error occurs.
- 4: Disables notifications.

默认值为 1|2。

```yaml
Type: NotifyFlagValue
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Priority
用于设置 BITS（Binary Transfer Service）传输任务的优先级，该优先级会影响带宽的使用情况。此参数的可接受取值为：

- **Foreground** (default): Transfers the job in the foreground. Foreground transfers compete for network bandwidth with other applications, which can impede the user's overall network experience. However, if the **Start-BitsTransfer** cmdlet is being used interactively, this is likely the best option. This is the highest priority level.

- **High**: Transfers the job in the background with a high priority. Background transfers use the idle network bandwidth of the client computer to transfer files.

- **Normal**: Transfers the job in the background with a normal priority. Background transfers use the idle network bandwidth of the client computer to transfer files.

- **Low**: Transfers the job in the background with a low priority. Background transfers use the idle network bandwidth of the client to transfer files. This is the lowest background priority level.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Foreground, High, Normal, Low

Required: False
Position: Named
Default value: Foreground
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyAuthentication
指定在Web代理上使用的身份验证机制。该参数的可接受值为：

- **Basic**: Basic is a scheme in which the user name and password are sent in clear-text to the server or proxy.

- **Digest**: Digest is a challenge-response scheme that uses a server-specified data string for the challenge.

- **Ntlm**: NTLM is a challenge-response scheme that uses the credentials of the user for authentication in a Windows-based network environment.

- **Negotiate** (the default): Negotiate is a challenge-response scheme that negotiates with the server or proxy to determine which scheme to use for authentication. For instance, this parameter value allows negotiation to determine whether the Kerberos protocol or NTLM is used.

- **Passport**: Passport is a centralized authentication service provided by Microsoft that offers a single logon for member sites.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Basic, Digest, Ntlm, Negotiate, Passport

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyBypass
指定用于直接连接的主机名称列表。系统会按顺序尝试列表中的各个主机，直到建立成功连接为止。如果指定了此参数，则该 cmdlet 会绕过代理服务器。在使用此参数时，必须将 *ProxyUsage* 参数设置为 **Override**；否则会导致错误。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyCredential
指定用于在代理服务器上验证用户身份的凭据。您可以使用 **Get-Credential** cmdlet 来为该参数创建相应的值。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyList
指定要使用的代理列表。列表中的代理会按顺序尝试，直到建立成功连接为止。如果指定了此参数，并且 *ProxyUsage* 的值设置为除 **Override** 以外的其他值，则该 cmdlet 会生成错误。

```yaml
Type: Uri[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyUsage
指定代理使用设置。该参数的可接受值为：

- **SystemDefault** (the default): Use the system default proxy settings.

- **NoProxy**: Do not use a proxy to transfer files. Use this option when you transfer files within a local area network (LAN).

- **AutoDetect**: Automatically detect proxy settings. BITS detects proxy settings for each file in the job.

- **Override**: Specify the proxies or servers to use. If the *ProxyList* parameter is also specified, the proxies in that list are used. If the *ProxyBypass* parameter is also specified, the servers in that list are used. In both cases, the first member of the list is used. If the first member is unreachable, the subsequent members are tried until a member is contacted successfully.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: SystemDefault, NoProxy, AutoDetect, Override

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RetryInterval
该参数指定在BITS遇到临时性错误后，再次尝试传输文件之前需要等待的最短时间（以秒为单位）。允许的最小值为60秒。如果此值超过了**BitsJob**对象中设置的RetryTimeout属性所指定的值，BITS将不会重新尝试传输文件，而是会将BITS传输作业的状态设置为“Error”（错误）状态。

默认值为 600 秒（10 分钟）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RetryTimeout
该参数指定了在首次出现临时错误后，BITS尝试传输文件的时间长度（以秒为单位）。将重试周期设置为 0 可以避免重复尝试；当发生错误时，作业会强制进入 `BG_JOB_STATE_ERROR` 状态。如果重试周期的值超过了 `JobInactivityTimeout` 组策略设置（默认为 90 天），BITS 将在超过该时间限制后取消该作业。

默认值为 1,209,600 秒（14 天）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SecurityFlags
指定HTTP请求的安全标志。

你可以设置的标志位（从最低有效位开始）如下所示：

- 1: Enable CRL Check.
- 2: Ignore incorrect common names in the server certificate.
- 3: Ignore incorrect dates in the server certificate.
- 4: Ignore incorrect certification authorities in the server certificate.
- 5: Ignore incorrect usage of the server certificate.
- 12: Allow redirection from HTTPS to HTTP.

使用第9位到第11位的比特来实施你的重定向策略：

- 0,0,0: Redirects are automatically allowed.
- 0,0,1: Remote name is updated if a redirect occurs.
-0,1,0: BITS fails the job if a redirect occurs.

```yaml
Type: SecurityFlagValue
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Source
请指定您想要传输的文件的来源位置及其名称。源文件名会与相应的目标文件名配对。例如，*Source* 参数中指定的第一个文件名对应于 *Destination* 参数中的第一个文件名，而 *Source* 参数中的第二个文件名则对应于 *Destination* 参数中的第二个文件名。*Source* 和 *Destination* 参数必须具有相同数量的元素；否则，该命令会生成错误。您可以使用标准的通配符（如星号 (*) 和问号 (?)），或者使用范围操作符（如 “\[a-r\]”）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Suspended
该命令表示会暂停 BITS（BitTorrent Transfer Service）传输任务。如果未指定 `Suspended` 参数，传输任务将自动开始；如果指定了 `Suspended` 参数，那么在创建了 BITS 传输任务后，命令提示符会立即返回到正常状态。你可以使用 `Resume-BitsTransfer` 命令来重新启动传输任务。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TransferPolicy
指定允许调度数据传输的网络成本状态。当前网络的成本状态是一个位掩码（bitmap），该掩码表明如果在此时间安排数据传输会产生的费用类型。这个成本状态实际上就是一个位掩码：如果与当前网络成本状态对应的位被设置为“1”，则可以调度数据传输；如果该位未被设置为“1”，则数据传输将不会被考虑用于调度。您可以使用此处列出的任何值，或者将这些值组合起来以生成一个自定义的值。

该参数的可接受值为：

- **Unrestricted** (or unknown) : 0x00000001 : the cost state for this network is not known.

- **Capped** : 0x00000002 : the cost state for this network is a capped plan, or a plan that has a data usage limit.

- **BelowCap** : 0x00000004 : the cost state for this network is below the data plan cap.

- **NearCap** : 0x00000008 : the cost state for this network is near the data plan cap.

- **OverCapCharged** : 0x00000010 : the cost state for this network is above the data plan cap, and such usage is charged.

- **OverCapThrottled** : 0x00000020 : the cost state for this network is above the data plan cap, and such usage is throttled.

- **UsageBased** : 0x00000040 : the cost state for this network is charged based on usage.

- **Roaming** : 0x00000080 : the cost state for this network incurs roaming charges.
The cost state also includes one option (IgnoreCongestion) and a set of standard policies (Uncosted, Standard, NoSurcharge, NotRoaming, and Always) which are combinations of the discrete bit values.

- **IgnoreCongestion** : 0x80000000 : the job can be scheduled even if the network provider reports that the network is congested.

- **PolicyUnrestricted** : 0x80000021 : the set of cost states that do not consume the quota of a capped plan, or incur extra charges.

- **Standard** : 0x80000067 : a set of cost states suitable for moderate-priority transfers.

- **NoSurcharge** : 0x8000006f : the set of cost states that incur no surcharge for use.

- **NotRoaming** : 0x8000007f : the set of cost states that exclude the roaming state.

- **Always** : 0x800000ff : the set of all cost states.

成本状态还包括一个选项（忽略拥塞情况）以及一组标准策略（始终启用、不允许漫游、不收取额外费用、标准模式和免费模式），这些策略都是离散位值的组合。

```yaml
Type: CostStates
Parameter Sets: (All)
Aliases:
Accepted values: None, Unrestricted, Capped, BelowCap, NearCap, OverCapCharged, OverCapThrottled, UsageBased, Roaming, IgnoreCongestion, PolicyUnrestricted, Standard, NoSurcharge, NotRoaming, Always

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TransferType
指定 BITS 传输作业的类型。该参数可接受的值包括：

- **Download** (the default): Specifies that the transfer job downloads files to the client computer.

- **Upload**: Specifies that the transfer job uploads a file to the server.

- **UploadReply**: Specifies that the transfer job uploads a file to the server and receives a reply file from the server.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Download, Upload, UploadReply

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseStoredCredential
该参数指定：当指定的目标服务器类型需要身份验证时，应使用存储在 Windows 凭据管理器中的凭据进行认证。如果未指定此参数且服务器确实需要进行身份验证，则必须通过使用 *Credential* 或 *ProxyCredential* 参数来明确提供所需的凭据。此参数是一个标志型参数，其不同的取值可以组合使用以实现所需的行为。

该参数的可接受值为：

- **None**: Use only credentials provided by the *Credential* or *ProxyCredential* parameters.
This is the default behavior if the parameter is not specified.

- **Proxy**: Credentials stored in the Windows Credential Manager are used for authentication for any proxy server that requires authentication.
If no credentials in the Windows Credential Manager match the proxy server needing authentication, then you must specify credentials by using the *ProxyCredential* parameter.

- **Server**: This value is not supported and generates an error if specified.

```yaml
Type: AuthenticationTargetValue
Parameter Sets: (All)
Aliases:
Accepted values: None, Server, Proxy

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无
此cmdlet不接受任何输入参数。

## 输出

### Microsoft.BackgroundIntelligentTransfer.Management.BitsJob
当使用“Asynchronous”参数调用此cmdlet时，它会输出与新的BITS传输任务相关联的**BitsJob**对象；否则，不会生成任何输出。

## 备注
* You can cancel a transfer job that is running in synchronous mode by pressing CTRL+C.

如果在同步文件传输任务进行过程中BITS服务被停止，那么该文件传输任务将会失败，并且会一直保留在BitsTransfer队列中。你可以使用**Get-BitsTransfer** cmdlet查看仍然存在于 BitsTransfer 队列中的文件传输任务。可以使用**Remove-BitsTransfer** cmdlet来删除这些任务。一旦BITS服务重新启动，文件传输任务将会继续执行（除非在此期间该任务已被手动删除）。

## 相关链接

[Add-BitsFile](./Add-BitsFile.md)

[完成位传输](./Complete-BitsTransfer.md)

[Get-BitsTransfer](./Get-BitsTransfer.md)

[Remove-BitsTransfer](./Remove-BitsTransfer.md)

[Resume-BitsTransfer](./Resume-BitsTransfer.md)

[Set-BitsTransfer](./Set-BitsTransfer.md)

[暂停位传输](./Suspend-BitsTransfer.md)

