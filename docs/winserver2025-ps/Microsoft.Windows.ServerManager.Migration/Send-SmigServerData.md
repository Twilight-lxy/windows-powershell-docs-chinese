---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.ServerManager.PowerShell.dll-Help.xml
Module Name: Microsoft.Windows.ServerManager.Migration
ms.date: 01/03/2017
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.servermanager.migration/send-smigserverdata?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Send-SmigServerData
---

# Send-SmigServerData

## 摘要
通过端口7000，将文件夹、文件及其相关的权限和共享属性从源服务器迁移到目标服务器。在源服务器上运行`Send-SmigServerData`命令的同时，必须在目标服务器上运行`Receive-SmigServerData`命令。

## 语法

```
Send-SmigServerData -ComputerName <String> -Password <SecureString> -Include <MigrationIncludeTypes>
 -DestinationPath <String> [-Force] [-Recurse] -SourcePath <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Send-SmigServerData` cmdlet 可以通过端口 7000 将文件夹、文件及其关联的权限和共享属性从本地服务器迁移到目标服务器。为了接收数据，必须在目标服务器上运行 `Receive-SmigServerData` cmdlet。默认情况下，`Send-SmigServerData` 最多会等待五分钟来与目标服务器上的 `Receive-SmigServerData` 建立连接。您可以使用注册表键来更改这个默认的最大连接时间；有关此注册表设置的更多信息，请参阅“备注”部分。

在本次发布的 Windows Server 中，您可以在这些服务器之间发送和接收数据（这些服务器不一定位于同一个子网中）。您还可以使用 IP 地址来指定源服务器或目标服务器的名称。为了支持跨子网的迁移，并通过 IP 地址来进行迁移操作，必须在源服务器和目标服务器上打开端口 7001 和 7002。

文件访问权限在迁移过程中会得到保留；迁移完成后，同一组用户仍然能够访问目标服务器上的文件。由于文件是通过加密连接传输的，因此需要在源服务器和目标服务器上提供密码才能解密这些文件。不支持传输加密文件（EFS）和链接点。

有关[Windows PowerShell中的服务器迁移cmdlet](https://go.microsoft.com/fwlink/?LinkId=246313)的在线帮助，请访问：http://go.microsoft.com/fwlink/?LinkId=246313。

## 示例

#### 示例 1：发送文件
```
PS C:\> Send-SmigServerData -Include Data -ComputerName "Server2" -SourcePath "c:\users" -DestinationPath "d:\shares\users" -Verbose
```

这个示例命令会将本地（源）计算机上 c:\users 文件夹中的所有文件迁移到目标计算机上的 d:\shares\users 文件夹中。默认情况下，c:\users 文件夹中的子文件夹不会被传输。该命令使用参数 *ComputerName* 中指定的计算机名称 “Server2” 来在子网中查找目标服务器。

由于这个示例命令中没有提供密码，在输入命令后，系统会提示用户输入用于加密迁移数据的密码。密码字符会以星号（*）的形式显示。当用户输入密码后，该密码会被作为 `SecureString` 类型传递给命令执行。

通过使用 `Verbose` 参数，该命令还会显示有关迁移操作的详细信息。

### 示例 2：创建一个密码变量，并使用它来发送文件
```
PS C:\> $pass = ConvertTo-SecureString -String "password" -AsPlainText -Force
PS C:\> Send-SmigServerData -Include Share -ComputerName "Server2" -SourcePath "c:\users" -DestinationPath "d:\shares\users" -Recurse -Password $pass -Verbose
```

在这个例子中，命令的第一行指示迁移工具将数据加密密码（用 “password” 表示）转换为一个安全的字符串，并将其存储在变量 $pass 中。

第二个示例命令仅迁移文件夹 `c:\users` 及其所有子文件夹的共享状态和权限，这是通过使用 `*Include` 和 `*Recurse` 参数实现的。`c:\users` 文件夹中的文件和子文件夹本身不会被迁移。该命令还将第一个命令中指定的变量 `$pass` 的值设置为用于加密数据传输的密码。命令使用 `ComputerName` 参数中提供的计算机名称 `Server2` 来在子网中查找目标服务器。

通过使用 `Verbose` 参数，该命令还会显示有关迁移操作的详细信息。

### 示例 3：发送文件并包含子文件夹
```
PS C:\> Send-SmigServerData -Include All -ComputerName "Server2" -SourcePath "c:\users" -DestinationPath "d:\shares\users" -Recurse -Password (Read-Host "Enter a Password:" -AsSecureString) -Verbose
```

在这个例子中，该命令将本地服务器上C:\users文件夹中的所有迁移数据迁移到远程服务器Server2上的D:\shares\users文件夹中。由于添加了*Recurse*参数，因此该命令还会迁移源文件夹子文件夹中的数据。为了在数据传输到目标服务器时对其进行加密，还添加了*Password*参数。*Password*参数的实际值是一个第二个命令：`(Read-Host "请输入密码：" -AsSecureString)`，用于提示管理员输入密码，并将输入的密码加密为安全字符串。最后，添加了*Verbose*参数以显示关于该命令操作和进度的详细信息。

## 参数

### -ComputerName
指定要复制数据的目标服务器的名称或 IP 地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationPath
指定目标服务器上用于复制数据的路径。为避免迁移失败，请确认您指定的目标路径确实存在（仅适用于共享迁移类型）；对于其他类型的迁移，请确保该路径能够在目标计算机上创建。该路径必须是有效的本地路径，且长度不得超过246个字符。系统不支持通配符字符。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
如果您从源服务器迁移的文件更新了，系统会自动覆盖现有的文件。同样地，如果目标服务器上已经存在相应的共享文件夹名称，系统也会覆盖这些共享文件夹的属性。

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

### -Include
指定要复制到目标服务器的内容类型。该参数可接受以下值：


- Data: Copies only files in the folder designated by the *SourcePath* parameter to the folder designated by the *DestinationPath* parameter.
Subfolders and their content are not copied unless the *Recurse* parameter is added.

- Share: Copies only the share properties assigned to the folder specified in the *SourcePath* parameter to the folder specified in the *DestinationPath* parameter.
For example, if a folder was shared on the source server, it is shared on the destination server if the Share value is provided in the cmdlet, thereby preserving all share properties and permissions.
Share properties for subfolders and their content are not copied unless the *Recurse* parameter is added.
The files and subfolders in the folder designated by *SourcePath* are not migrated.
To avoid migration failures, verify that the folder specified in the *DestinationPath* parameter (and all subfolders if the *Recurse* parameter is added) exists.
- All: Copies both data and associated share properties.

```yaml
Type: MigrationIncludeTypes
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Password
指定密码（以安全字符串的形式），用于使用 256 位高级加密标准（AES）对数据传输进行加密。该安全字符串可以通过输入命令 `Read-Host -AsSecureString` 或 `ConvertTo-SecureString` 来获取。

你必须指定一个密码来保护你的数据，因为传输的数据是通过网络广播的。如果你在命令中没有添加“Password”参数，在输入命令后系统会提示你输入密码。密码的长度必须至少为6个字符，最多为260个字符。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Recurse
将 *Include* 参数所指定的类型的全部内容复制到 *SourcePath* 参数中指定的路径中。如果未使用该参数，则不会复制 *SourcePath* 下的子文件夹。

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

### -SourcePath
指定源服务器上用于复制数据的文件夹。为避免迁移失败，您需要先确认所指定的源路径确实存在于源计算机上（仅限“共享访问”类型的迁移除外）。该路径必须是有效的本地路径，且长度不能超过246个字符。系统不支持通配符字符。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Windows.ServerManager.MigrationCommands.MigrationResult []
`MigrationResult` 对象包含关于请求的迁移操作是否成功的基本信息。

## 备注
* The Windows Server Migration Tools deployment log file is located in %windir%\Logs\SmigDeploy.log. Other Windows Server Migration Tools log files are created at the following locations:


- %windir%\Logs\ServerMigration.log

- On Windows Server 2008 and later versions: %localappdata%\SvrMig\Log

- On Windows Server 2003: %userprofile%\Local Settings\Application Data\SvrMig\Log

如果这些位置无法创建日志文件，则 ServerMigration.log 和 SmigDeploy.log 将会被创建在 %temp% 目录下，其他日志文件则会被创建在 %windir%\System32 目录下。

所有日志文件的最大大小（以MB为单位）存储在以下注册表键中。当日志文件的大小超过注册表键中指定的值时，该日志文件会被删除。随后会使用相同的文件名和路径创建一个新的日志文件，并重新开始记录数据。默认的最大日志文件大小为200 MB。


- Key: HKLM\Software\Microsoft\ServerMigration

- Value: MaxLogSize (REG_DWORD)

- Data: Whole numbers between 1 and 1000 (represents log size, in MB)

`Send-SmigServerData` 和 `Receive-SmigServerData` cmdlet 的最大连接时间存储在以下注册表键中。如果在指定时间内无法建立连接，`Send-SmigServerData` 和 `Receive-SmigServerData` 操作将会终止。默认的最大连接时间为 300 秒（即五分钟）。


- Key: HKLM\Software\Microsoft\ServerMigration

- Value: MaxConnectionTime  (REG_DWORD)

- Data: Between 1 and 3600 (represents connection time, in seconds).
If a value larger than 3600 is specified, 3600 seconds is used as the maximum connection time.

## 相关链接

[接收迁移服务器数据](./Receive-SmigServerData.md)

