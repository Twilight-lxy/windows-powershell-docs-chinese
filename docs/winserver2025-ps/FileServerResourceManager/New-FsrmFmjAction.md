---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmFmjAction.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmfmjaction?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmFmjAction
---

# New-FsrmFmjAction

## 摘要
返回一个用于文件管理作业的动作对象。

## 语法

```
New-FsrmFmjAction [-Type] <FmjActionTypeEnum> [-ExpirationFolder <String>] [-RmsFolderOwner]
 [-RmsFullControlUser <String[]>] [-RmsReadUser <String[]>] [-RmsWriteUser <String[]>] [-RmsTemplate <String>]
 [-Command <String>] [-WorkingDirectory <String>] [-CommandParameters <String>]
 [-SecurityLevel <FmjActionSecurityLevelEnum>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmFmjAction` cmdlet 返回一个对象，你可以使用该对象来创建文件管理作业操作。你可以在 `New-FsrmFileManagementJob` cmdlet 和 `Set-FsrmFileManagementJob` cmdlet 中将 `FsrmFmjAction` 对象作为输入参数使用。

`FsrmFmjAction` 对象定义了文件管理任务在处理文件时所执行的一种操作。该 cmdlet 支持以下操作：

- Expiration.
Move the file to another location.
- RMS.
Encrypt the file (Rights Management Services).
- Custom.
Run a command.

## 示例

### 示例 1：创建一个用于删除过期文件的动作
```
PS C:\> New-FsrmFmjAction -Type Expiration -ExpirationFolder "C:\shares\expire01"
```

此命令返回一个对象，该对象会将文件删除到路径 C:\shares\expire01。

### 示例 2：创建一个使用 RMS 模板对文件进行加密的操作
```
PS C:\> New-FsrmFmjAction -Type RMS -RmsTemplate "Contoso Confidential"
```

这个命令返回一个动作对象，该对象用于将文件加密为 Contoso Confidential RMS 模板格式。执行此命令之前，需要在名为“Contoso Confidential”的 RMS 服务器上配置相应的 RMS 模板。

#### 示例 3：创建一个用于加密文件并设置 RMS 权限的操作
```
PS C:\> New-FsrmFmjAction -Type RMS -RmsFullControlUser "admin@contoso.com" -RmsReadUser "AllStaff@contoso.com" -RmsWriteUser "AllFTE@contoso.com"
```

该命令返回一个操作对象，用于加密文件。这样，在 contoso.com 中的管理员账户将对该文件拥有完全控制权；ALLFTE 安全组对该文件具有编辑权限；而 ALLStaff 组对该文件具有读取权限。

### 示例 4：创建一个用于运行命令的操作
```
PS C:\> New-FsrmFmjAction -Type Custom -Command "C:\windows\system32\cmd.exe" -CommandParameters "echo [source file path] >> c:\log.txt"
```

该命令返回一个动作对象，用于运行 Cmd.exe 并指定命令的参数。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Command
指定该操作要执行的命令。如果您指定了一个命令，则必须将“Type”参数设置为“Custom”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CommandParameters
指定当该动作运行时传递给命令的参数。如果您为某个命令指定了参数，则必须将“类型”（Type）参数设置为“自定义”（Custom）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

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

### -ExpirationFolder
指定一个路径，该动作将使用此路径来删除过期的文件。如果您指定了一个用于存放过期文件的文件夹，则必须为“类型”（Type）参数设置“过期”（Expiration）属性。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RmsFolderOwner
表示该操作会将RMS文件夹所有者（FolderOwner）添加到“完全控制”权限列表中。如果某个文件没有对应的文件夹所有者，此设置将不起作用。

如果您指定了一个 RMS 文件夹所有者，那么必须为 “Type” 参数指定 “RMS”。如果您指定了该参数，则不要指定 “RMSFullControlUser”、“RMSReadUser” 或 “RMSWriteUser” 参数。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RmsFullControlUser
用于指定一个电子邮件地址数组，以便对 Active Directory 权限管理服务（AD RMS）的加密功能进行完全控制。如果使用了此cmdlet，则必须为*Type*参数指定“RMS”；但如果指定了该参数，则不得再指定*RMSTemplate*参数。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RmsReadUser
用于指定一组地址，以授予这些地址对 Active Directory Rights Management Services (AD RMS) 加密的读取权限。如果您使用了此 cmdlet，则必须为 *Type* 参数指定 “RMS”；但如果指定了该参数，则不得再指定 *RMSTemplate* 参数。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RmsTemplate
指定该操作应用于文件的RMS模板的名称。如果指定了RMS模板，则必须为*Type*参数指定“RMS”。如果指定了此参数，就不要再指定*RMSFullControlUser*、*RMSReadUser*或*RMSWriteUser*参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RmsWriteUser
指定一个地址数组，以赋予这些地址对 Active Directory 权限管理服务（AD RMS）加密功能的写入权限。如果您使用了此cmdlet，则必须为*Type*参数指定“RMS”选项；如果指定了该参数，则不要再指定*RMSTemplate*参数。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SecurityLevel
指定系统账户，该账户将用于运行您在“Command”参数中指定的命令。如果您指定了此参数，则必须将“Type”参数设置为“Custom”。

```yaml
Type: FmjActionSecurityLevelEnum
Parameter Sets: (All)
Aliases:
Accepted values: None, NetworkService, LocalService, LocalSystem

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的命令行函数（cmdlet）的最大操作数量。如果省略此参数或输入值为`0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令行函数的数量来计算出一个最优的并发限制。这个并发限制仅适用于当前正在执行的命令行函数，而不影响整个会话或计算机本身。

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

### -Type
指定文件管理作业执行的操作类型。该参数的可接受值为：

- Expiration
- RMS
- Custom

```yaml
Type: FmjActionTypeEnum
Parameter Sets: (All)
Aliases:
Accepted values: Expiration, Custom, Rms

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
Shows what would happen if the cmdlet runs.
The cmdlet is not run.

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

### -WorkingDirectory
Specifies the working directory in which the program or script runs.
You must specify a valid path to a folder.
File Server Resource Manager (FSRM) does not support paths to remote computers.
If you specify this parameter, you must specify Custom for the *Type* parameter.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.PowerShell CmdletizationGeneratedTypes.FmjActionTypeEnum

### System.String

### System.Management.Automation.SwitchParameter

### System.String[]

### Microsoft.PowerShell Cmdletization GeneratedTypes.FmjActionSecurityLevelEnum

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[New-FsrmFileManagementJob](./New-FsrmFileManagementJob.md)

[Set-FsrmFileManagementJob](./Set-FsrmFileManagementJob.md)

