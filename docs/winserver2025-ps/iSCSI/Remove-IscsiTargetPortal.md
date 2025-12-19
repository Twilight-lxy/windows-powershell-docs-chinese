---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: iSCSITargetPortal.cdxml-help.xml
Module Name: iSCSI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsi/remove-iscsitargetportal?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IscsiTargetPortal
---

# 移除IscsiTargetPortal

## 摘要
删除指定的 iSCSI 目标端口。

## 语法

### 根据目标门户地址（默认值）
```
Remove-IscsiTargetPortal -TargetPortalAddress <String[]> [-InitiatorInstanceName <String>]
 [-InitiatorPortalAddress <String>] [-TargetPortalPortNumber <Int32>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Remove-IscsiTargetPortal -InputObject <CimInstance[]> [-InitiatorInstanceName <String>]
 [-InitiatorPortalAddress <String>] [-TargetPortalPortNumber <Int32>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-IscsiTargetPortal` cmdlet 用于删除现有的 iSCSI 目标端口连接。

## 示例

### 示例 1：移除目标门户
```
PS C:\> Get-IscsiTargetPortal
InitiatorInstanceName      :
InitiatorNodeAddress       :
InitiatorPortalAddress     :
InititorIPAdressListNumber : 4294967295
IsDataDigest               : False
IsHeaderDigest             : False
TargetPortalAddress        : testIscsi
TargetPortalPortNumber     : 3260 PS C:\> Remove-IscsiTargetPortal -TargetPortalAddress "testIscsi"
```

这个示例用于删除一个目标门户（target portal）。

第一个命令使用 **Get-IscsiTargetPortal** cmdlet 显示目标门户的信息。该目标门户的地址为 testIscsi。

第二个命令会删除地址为“testIscsi”的目标门户（portal）。

## 参数

### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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
在运行该cmdlet之前，会提示您进行确认。

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

### -InitiatorInstanceName
指定 iSCSI 启动器服务用于向目标门户发送 **SendTargets** 请求的启动器实例的名称。如果未指定实例名称，则 iSCSI 启动器服务会自行选择相应的启动器实例。

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

### -InitiatorPortalAddress
指定与发起者门户相关联的 IP 地址或 DNS 名称。

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

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

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

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -TargetPortalAddress
指定目标门户的 IP 地址或 DNS 名称。

```yaml
Type: String[]
Parameter Sets: ByTargetPortalAddress
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetPortalPortNumber
指定目标门户的TCP/IP端口号。默认情况下，端口号为3260。

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

### -ThrottleLimit
指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[TechNet上的iSCSI相关内容](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee338476(v=ws.10))

[TechNet上的存储相关内容](https://go.microsoft.com/fwlink/?linkid=191356)

[Get-IscsiTargetPortal](./Get-IscsiTargetPortal.md)

