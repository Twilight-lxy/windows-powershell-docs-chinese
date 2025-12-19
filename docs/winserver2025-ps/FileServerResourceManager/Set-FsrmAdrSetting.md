---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmAdrSetting.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/set-fsrmadrsetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-FsrmAdrSetting
---

# Set-FsrmAdrSetting

## 摘要
更改配置设置，以解决访问被拒绝的问题。

## 语法

### 查询（cdxml）（默认值）
```
Set-FsrmAdrSetting [-Event] <FsrmAdrEventEnum[]> [-Enabled] [-DisplayMessage <String>] [-EmailMessage <String>]
 [-AllowRequests] [-MailToOwner] [-MailCCAdmin] [-MailTo <String>] [-IncludeDeviceClaims] [-IncludeUserClaims]
 [-EventLog] [-DeviceTroubleshooting] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-FsrmAdrSetting -InputObject <CimInstance[]> [-Enabled] [-DisplayMessage <String>] [-EmailMessage <String>]
 [-AllowRequests] [-MailToOwner] [-MailCCAdmin] [-MailTo <String>] [-IncludeDeviceClaims] [-IncludeUserClaims]
 [-EventLog] [-DeviceTroubleshooting] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-FsrmAdrSetting` cmdlet 用于更改一个或多个事件的访问权限拒绝修复（Access Denied Remediation, ADR）相关配置设置。当客户端无法访问文件时，文件服务器资源管理器（File Server Resource Manager, FSRM）会使用这些 ADR 设置。如果用户尝试访问他们没有权限的文件服务器上的共享文件和文件夹，将会收到“访问被拒绝”的提示信息。

## 示例

#### 示例 1：更改某个事件的 ADR 设置
```
PS C:\> Set-FsrmAdrSetting -Event AccessDenied -Enabled -DisplayMessage "Access to file is denied" -EmailMessage "Access to file is denied. You can email a request for permission to access the file." -AllowRequests -MailToOwner:$false -MailCCAdmin -MailTo "john@contoso.com" -IncludeDeviceClaims -IncludeUserClaims -EventLog -DeviceTroubleShooting
```

此命令用于更改与 “AccessDenied” 事件相关的 ADR（自动故障恢复）设置。该命令启用了针对 “AccessDenied” 事件的补救措施，指定了该事件的显示消息和电子邮件内容，并表明用户可以通过发送电子邮件来请求访问权限。

## 参数

### -AllowRequests
表示用户可以通过发送电子邮件来申请访问权限。

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

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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

### -DeviceTroubleshooting
这表示在出现“访问被拒绝”错误消息时，Windows系统会向用户显示该设备所声称的身份或权限信息。

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

### -DisplayMessage
指定文件服务器在接收到该事件时向用户显示的消息内容。字符串的长度不得超过 10KB。

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

### -EmailMessage
指定文件服务器在接收到相应事件时发送给用户的电子邮件内容。该字符串的长度不得超过 10 KB。

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

### -Enabled
表示已为该服务器上的事件启用了修复功能（即当发生问题时可以采取相应的补救措施）。

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

### -Event
指定 ADR 处理的事件类型数组。该参数的可接受值为：AccessDenied 和 FileNotFound。

```yaml
Type: FsrmAdrEventEnum[]
Parameter Sets: Query (cdxml)
Aliases:
Accepted values: AccessDenied, FileNotFound

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EventLog
表示服务器会为文件服务器发送的每个访问请求电子邮件创建一条事件日志记录。

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

### -IncludeDeviceClaims
这表示当用户请求访问时，文件服务器会包含设备声明（device claims）。

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

### -IncludeUserClaims
表示当用户请求访问时，文件服务器会包含用户的身份信息（即“user claims”）。

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

### -InputObject
指定要传递给此cmdlet的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -MailCCAdmin
当用户请求访问时，这表示文件服务器会在电子邮件消息的抄送（CC）行中包含系统管理员的信息。

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

### -MailTo
指定一个用分号分隔的电子邮件地址列表，文件服务器会将请求发送到这些地址。

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

### -MailToOwner
表示当用户请求访问时，文件服务器会向数据所有者发送电子邮件。

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

### -PassThru
返回一个对象，该对象代表您正在操作的项。默认情况下，此 cmdlet 不生成任何输出。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.PowerShell Cmdletization GeneratedTypes.FsrmAdrEventEnum[]

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FSRMADRSettings

## 备注

## 相关链接

[Get-FsrmAdrSetting](./Get-FsrmAdrSetting.md)

