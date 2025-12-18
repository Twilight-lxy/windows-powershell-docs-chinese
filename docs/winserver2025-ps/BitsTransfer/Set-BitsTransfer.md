---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BackgroundIntelligentTransfer.Management.dll-Help.xml
Module Name: BitsTransfer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitstransfer/set-bitstransfer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-BitsTransfer
---

# Set-BitsTransfer

## 摘要
修改现有BITS传输作业的属性。

## 语法

```
Set-BitsTransfer [-BitsJob] <BitsJob[]> [-DisplayName <String>] [-Priority <String>] [-Description <String>]
 [-Dynamic] [-CustomHeadersWriteOnly] [-HttpMethod <String>] [-ProxyAuthentication <String>]
 [-RetryInterval <Int32>] [-RetryTimeout <Int32>] [-MaxDownloadTime <Int32>] [-TransferPolicy <CostStates>]
 [-ACLFlags <ACLFlagValue>] [-SecurityFlags <SecurityFlagValue>]
 [-UseStoredCredential <AuthenticationTargetValue>] [-Credential <PSCredential>]
 [-ProxyCredential <PSCredential>] [-Authentication <String>] [-SetOwnerToCurrentUser] [-ProxyUsage <String>]
 [-ProxyList <Uri[]>] [-ProxyBypass <String[]>] [-CustomHeaders <String[]>] [-NotifyFlags <NotifyFlagValue>]
 [-NotifyCmdLine <String[]>] [-CertStoreLocation <CertStoreLocationValue>] [-CertStoreName <String>]
 [-CertHash <Byte[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-BitsTransfer` cmdlet 用于修改现有的背景智能传输服务（Background Intelligent Transfer Service，简称 BITS）传输作业的属性。你可以通过 `BitsJob` 参数指定要修改的作业；或者，也可以通过管道将作业传递给该 cmdlet 来进行修改。

## 示例

### 示例 1：修改 BITS 传输作业的优先级
```
PS C:\> $Bits = Get-BitsTransfer -JobId 10778CFA-C1D7-4A82-8A9D-80B19224879C
PS C:\> Set-BitsTransfer -BitsJob $Bits -Priority High
```

这个命令用于修改现有的BITS传输作业的优先级。

第一个命令会根据*JobId*参数检索指定的BITS传输任务，然后将其存储在$Bits变量中。

第二个命令使用了 *BitsJob* 参数，将存储在 $Bits 变量中的 **BitsJob** 对象传递给 **Set-BitsTransfer** cmdlet。*Priority* 参数用于将 BITS 传输作业的优先级设置为“高”（High）。

### 示例 2：设置一组 BITS 转移作业的所有者
```
PS C:\> Get-BitsTransfer -AllUsers -Name *Microsoft* | Set-BitsTransfer -SetOwnerToCurrentUser
```

这个命令将当前用户设置为一组现有的BITS传输作业的所有者。

`Get-BitsTransfer` cmdlet 的输出是一组 `BitsJob` 对象，这些对象的显示名称中包含 “Microsoft” 字样。这些输出结果会通过管道传递给 `Set-BitsTransfer` cmdlet。`SetOwnerToCurrentUser` 参数指定每个 BITS 传输作业的所有者均为当前用户。

### 示例 3：修改 BITS 传输任务的代理设置
```
PS C:\> $Bits = Get-BitsTransfer -JobId 10778CFA-C1D7-4A82-8A9D-80B19224879C
PS C:\> $Cred = Get-Credential
PS C:\> Set-BitsTransfer -BitsJob $Bits -ProxyUsage AutoDetect -ProxyAuthentication $Cred
```

此命令会修改现有BITS传输任务的代理设置。

第一个命令会根据*JobId*参数获取相应的BITS传输任务，并将其存储在名为$Bits的变量中。

第二个命令从用户那里获取凭据，然后将它们存储在 `$Cred` 变量中。

第三个命令使用了 *BitsJob* 参数，将存储在 $Bits 变量中的 **BitsJob** 对象传递给 **Set-BitsTransfer** cmdlet。它还使用了 *ProxyAuthentication* 参数，将存储在 $Cred 变量中的 **PSCredential** 对象传递给该 cmdlet。*ProxyUsage* 参数允许 BITS 传输任务通过使用 Web Proxy 自发现协议（WPAD）来自动查找 Web 代理服务器。所提供的凭据用于在代理服务器上对用户进行身份验证。

### 示例 4：使用代理列表和代理绕过功能来修改 BITS 传输任务的代理设置
```
PS C:\> Get-BitsTransfer | Set-BitsTransfer -ProxyUsage Override -ProxyList "http://proxy1", "http://proxy2:81" -ProxyBypass "http://directconnect"
```

此命令会修改现有BITS传输任务的代理设置。

`Get-BitsTransfer` cmdlet 的输出是一组由当前用户拥有的 `BitsJob` 对象。这些输出会被传递给 `Set-BitsTransfer` cmdlet。在 `ProxyUsage` 参数中指定的 `Override` 值表示提供了代理服务器和被绕过的主机名称的显式列表。

`ProxyList` 参数指定了两台代理服务器。列表中的第一台服务器（`http://proxy1`）会被优先使用。如果该连接失败，命令会尝试使用列表中的第二台服务器（`http://proxy2:81`）进行连接。如果这两台服务器的连接都失败了，那么任务也会失败。

当在*ProxyBypass*参数中指定了一组主机名时，建立的连接将是一个不使用代理服务器的直接连接。在这个例子中，没有使用任何代理服务器来将文件添加到directconnect服务器上的BITS传输队列中。

## 参数

### -ACLFlags
指定转移作业的所有者和访问控制列表（ACL）信息。请指定以下一个或多个值：

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

### -Authentication
指定在服务器上使用的认证机制。该参数的可接受值如下：

- **Basic**: Basic is a scheme in which the user name and password are sent in clear text to the server or proxy.

- **Digest**: Digest is a challenge-response scheme that uses a server-specified data string for the challenge.

- **NTLM**: NT LAN Manager (NTLM) is a challenge-response scheme that uses the credentials of the user for authentication in a Windows-based network environment.

- **Negotiate** (the default): Negotiate is a challenge-response scheme that negotiates with the server or proxy to determine which scheme to use for authentication. For example, this parameter value allows negotiation to determine whether the Kerberos protocol or NTLM is used.

- **Passport**: Passport is a centralized authentication service provided by Microsoft that offers a single logon for member sites.

```yaml
Type: String
Parameter Sets: (All)
Aliases: au
Accepted values: Basic, Digest, Ntlm, Negotiate, Passport

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -BitsJob
指定一个包含多个 BITS 传输作业的数组，此 cmdlet 将对这些作业设置属性。您可以将来自其他返回 **BitsJob** 对象的 cmdlet 的结果通过管道（pipe）传递给此参数，例如 Get-BitsTransfer。

```yaml
Type: BitsJob[]
Parameter Sets: (All)
Aliases: b

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -CertHash
指定一个用于标识证书的SHA1哈希值。

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
在运行cmdlet之前，会提示您进行确认。

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
指定用于在服务器上验证用户身份的凭据。默认值是当前用户。可以输入用户名，例如“User01”、“Domain01\User01”或“User@Contoso.com”。或者，可以使用 **Get-Credential** cmdlet 来生成该参数所需的值。当您输入用户名时，系统会要求您提供密码。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases: cred

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CustomHeaders
指定一个或多个自定义的HTTP头部，这些头部将包含在发送到服务器的请求中。请提供一个字符串数组作为参数。

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
表示此任务的HTTP自定义头部只能写入，无法读取。

当你的自定义头部包含安全信息时，请使用此参数。同一台计算机上的其他程序无法读取这些头部信息。BITS进程可以读取这些头部信息，并通过HTTP连接将其发送出去。

一旦您将作业的头部设置为“只读”模式，就无法再更改该值了。

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
为BITS传输作业指定一个描述。该描述的长度限制为1,024个字符。

```yaml
Type: String
Parameter Sets: (All)
Aliases: d

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisplayName
为BITS传输作业指定一个显示名称。该显示名称有助于用户更直观地区分不同的BITS传输作业。

```yaml
Type: String
Parameter Sets: (All)
Aliases: dn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Dynamic
表示该转账使用了动态设置。

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
指定一种不同于默认方法（GET）的数据传输方式。如果指定了 GET 方法，则该参数无效。

如果您指定了一个方法，该作业将获得前台优先级，且此优先级无法更改。

```yaml
Type: String
Parameter Sets: (All)
Aliases: hm

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxDownloadTime
指定一个作业中传输文件的最大时间（以秒为单位）。默认值为 7,776,000 秒，即 90 天。

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
指定一个在作业完成或遇到错误后运行的程序。该程序在运行此cmdlet的用户上下文中执行。

请将程序名称以及任何参数作为字符串数组来指定。

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

默认值是 1|2。

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
用于指定BITS传输任务的优先级，该优先级会影响带宽的使用情况。此参数的可接受值为：

- **Foreground** (default): Transfers the job in the foreground. Foreground transfers compete for network bandwidth with other applications, which can impede the user's overall network experience. However, if the **Start-BitsTransfer** cmdlet is being used interactively, this is likely the best option. This is the highest priority level.

- **High**: Transfers the job in the background with a high priority. Background transfers use the idle network bandwidth of the client computer to transfer files.

- **Normal**: Transfers the job in the background with a normal priority. Background transfers use the idle network bandwidth of the client computer to transfer files.

- **Low**: Transfers the job in the background with a low priority. Background transfers use the idle network bandwidth of the client to transfer files. This is the lowest background priority level.

```yaml
Type: String
Parameter Sets: (All)
Aliases: p
Accepted values: Foreground, High, Normal, Low

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyAuthentication
指定在Web代理上使用的身份验证机制。该参数的可接受值包括：

- **Basic**: Basic is a scheme in which the user name and password are sent in clear text to the server or proxy.

- **Digest**: Digest is a challenge-response scheme that uses a server-specified data string for the challenge.

- **NTLM**: NTLM is a challenge-response scheme that uses the credentials of the user for authentication in a Windows-based network environment.

- **Negotiate** (the default): Negotiate is a challenge-response scheme that negotiates with the server or proxy to determine which scheme to use for authentication. For instance, this parameter value allows negotiation to determine whether the Kerberos protocol or NTLM is used.

- **Passport**: Passport is a centralized authentication service provided by Microsoft that offers a single logon for member sites.

```yaml
Type: String
Parameter Sets: (All)
Aliases: pa
Accepted values: Basic, Digest, Ntlm, Negotiate, Passport

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyBypass
指定用于直接连接的主机名称列表。系统会按顺序尝试列表中的每个主机，直到建立成功连接为止。如果指定了此参数，该 cmdlet 会绕过代理服务器。在使用此参数时，必须将 *ProxyUsage* 参数设置为 **Override**；否则将会出现错误。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: pb

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyCredential
指定用于在代理服务器上验证用户身份的凭据。你可以使用 **Get-Credential** cmdlet 来生成此参数所需的值。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases: pc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyList
指定要使用的代理服务器数组。列表中的代理服务器会按顺序依次尝试，直到建立成功的连接为止。如果指定了此参数，并且 *ProxyUsage* 的值设置为除 “Override” 以外的其他值，则会发生错误。

```yaml
Type: Uri[]
Parameter Sets: (All)
Aliases: pl

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyUsage
指定代理使用设置。此参数的可接受值为：

- **SystemDefault** (the default): Use the system default proxy settings.

- **NoProxy**: Do not use a proxy to transfer the files. Use this option when you transfer files within a local area network (LAN).

- **AutoDetect**: Automatically detect proxy settings. BITS detects proxy settings for each file in the job.

- **Override**: Specify the proxies or servers to use. If the *ProxyList* parameter is also specified, the proxies in that list are used. If the *ProxyBypass* parameter is also specified, the servers in that list are used. In both cases, the first member of the list is used. If the first member is unreachable, the subsequent members are tried until a member is contacted successfully.

```yaml
Type: String
Parameter Sets: (All)
Aliases: pu
Accepted values: SystemDefault, NoProxy, AutoDetect, Override

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RetryInterval
该参数指定了在遇到临时错误后，BITS等待多长时间（以秒为单位）再尝试传输文件。允许的最小值为60秒。如果此值超过了**BitsJob**对象中设置的RetryTimeout值，BITS将不会重新尝试传输文件，而是会将BITS传输作业的状态设置为“Error”状态。

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
该参数指定了在首次出现临时错误后，BITS尝试传输文件的时间长度（以秒为单位）。将重试间隔设置为0可防止任何重试操作。如果重试间隔超过了“JobInactivityTimeout”组策略设置的值（默认为90天），BITS将会取消该任务。

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
用于指定 HTTP 请求的安全标志（security flags）。

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

### -SetOwnerToCurrentUser
表示该cmdlet将BITS传输作业的所有者设置为当前用户。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: so

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TransferPolicy
用于指定允许安排传输的网络成本状态。当前的网络成本状态是一个位掩码（bitmap），该掩码表明如果此时安排传输将会产生哪些类型的费用。这个成本状态实际上就是一个位掩码：如果与当前网络成本状态对应的位被设置（即该位为1），则可以安排传输；如果该位未被设置（即该位为0），则传输将不会被考虑用于调度。您可以提交这里列出的任何一种值，或者将这些值组合起来以生成一个自定义的值。

此参数的可接受值如下：

- **Unrestricted** (or unknown) : 0x00000001 : the cost state for this network is not known.

- **Capped** : 0x00000002 : the cost state for this network is a capped plan, or a plan that has a data usage limit.

- **BelowCap** : 0x00000004 : the cost state for this network is below the data plan cap.

- **NearCap** : 0x00000008 : the cost state for this network is near the data plan cap.

- **OverCapCharged** : 0x00000010 : the cost state for this network is above the data plan cap, and such usage is charged.

- **OverCapThrottled** : 0x00000020 : the cost state for this network is above the data plan cap, and such usage is throttled.

- **UsageBased** : 0x00000040 : the cost state for this network is charged based on usage.

- **Roaming** : 0x00000080 : the cost state for this network incurs roaming charges.

成本状态还包括一个选项（IgnoreCongestion）以及一组标准策略（Uncosted、Standard、NoSurcharge、NotRoaming 和 Always），这些标准策略是由离散的比特值组合而成的。

- **IgnoreCongestion** : 0x80000000 : the job can be scheduled even if the network provider reports that the network is congested.

- **PolicyUnrestricted** : 0x80000021 : the set of cost states that do not consume the quota of a capped plan, or incur extra charges.

- **Standard** : 0x80000067 : a set of cost states suitable for moderate-priority transfers.

- **NoSurcharge** : 0x8000006f : the set of cost states that incur no surcharge for use.

- **NotRoaming** : 0x8000007f : the set of cost states that exclude the roaming state.

- **Always** : 0x800000ff : the set of all cost states.

默认值是由作业优先级和组策略共同决定的。如果该值没有被明确设置，那么当作业优先级或当前组策略发生变化时，这个默认值也会随之改变。

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

### -UseStoredCredential
该参数指定：在需要针对指定的目标服务器类型进行身份验证时，应使用存储在 Windows 凭据管理器中的凭据。如果未指定此参数，而服务器又要求进行身份验证，则必须通过使用 *Credential* 或 *ProxyCredential* 参数来明确提供凭据。这是一个标志型参数，其不同的值可以组合使用以实现所需的行为。

此参数的可接受值如下：

- **None**: Use only credentials provided by the *Credential* or *ProxyCredential* parameters. This is the default behavior if the parameter is not specified.

- **Proxy**: Credentials stored in the Windows Credential Manager are used for authentication for any proxy server that requires authentication. If no credentials in the Windows Credential Manager match the proxy server needing authentication, then you must specify credentials by using the *ProxyCredential* parameter.

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.BackgroundIntelligentTransfer.Management.BitsJob[]
此cmdlet接受一个或多个**BitsJob**对象作为输入，并将这些对象填充到*BitsJob*参数中。

## 输出

### Microsoft.BackgroundIntelligentTransfer.Management.BitsJob[]
此cmdlet会生成与被修改的BITS传输任务相关联的**BitsJob**对象。

## 备注

## 相关链接

[Add-BitsFile](./Add-BitsFile.md)

[完成比特传输](./Complete-BitsTransfer.md)

[Get-BitsTransfer](./Get-BitsTransfer.md)

[Remove-BitsTransfer](./Remove-BitsTransfer.md)

[Resume-BitsTransfer](./Resume-BitsTransfer.md)

[开始比特传输](./Start-BitsTransfer.md)

[暂停位传输](./Suspend-BitsTransfer.md)

