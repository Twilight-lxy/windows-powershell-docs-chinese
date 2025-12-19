---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: iSCSITargetPortal.cdxml-help.xml
Module Name: iSCSI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsi/get-iscsitargetportal?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IscsiTargetPortal
---

# Get-IscsiTargetPortal

## 摘要
获取iSCSI目标端口（target portals）。

## 语法

### 按目标门户地址（默认值）
```
Get-IscsiTargetPortal [-InitiatorPortalAddress <String[]>] [[-TargetPortalAddress] <String[]>]
 [-InitiatorInstanceName <String[]>] [-TargetPortalPortNumber <UInt16[]>] [-IsHeaderDigest <Boolean[]>]
 [-IsDataDigest <Boolean[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByiSCSISession
```
Get-IscsiTargetPortal [-iSCSISession <CimInstance>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

### ByiSCSIConnection
```
Get-IscsiTargetPortal [-iSCSIConnection <CimInstance>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

### ByiSCSITarget
```
Get-IscsiTargetPortal [-iSCSITarget <CimInstance>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述
`Get-IscsiTargetPortal` cmdlet 可以获取有关 iSCSI 目标门户（iSCSI target portals）的信息。

## 示例

### 示例 1：获取有关 iSCSI 目标端口的信息
```
PS C:\> Get-IscsiTargetPortal -TargetPortalAddress "testIscsi"
InitiatorInstanceName      :
InitiatorNodeAddress       :
InitiatorPortalAddress     :
InititorIPAdressListNumber : 4294967295
IsDataDigest               : False
IsHeaderDigest             : False
TargetPortalAddress        : testIscsi
TargetPortalPortNumber     : 3260
```

这个命令用于获取名为“testiSCSI”的iSCSI目标门户的相关信息。

## 参数

### -AsJob
将该cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -InitiatorInstanceName
指定 iSCSI 启动器服务用于向目标门户发送 **SendTargets** 请求的启动器实例的名称。如果未指定实例名称，则 iSCSI 启动器服务会自行选择相应的启动器实例。

```yaml
Type: String[]
Parameter Sets: ByTargetPortalAddress
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InitiatorPortalAddress
指定与门户关联的IP地址或DNS名称。

```yaml
Type: String[]
Parameter Sets: ByTargetPortalAddress
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IsDataDigest
该参数用于指示当发起者登录目标门户时，此cmdlet是否启用数据摘要功能。如果您未指定此参数，则摘要功能的设置将由发起者的内核模式驱动程序决定。

```yaml
Type: Boolean[]
Parameter Sets: ByTargetPortalAddress
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IsHeaderDigest
该参数用于指示当发起者登录目标门户时，此 cmdlet 是否会启用头部摘要（header digest）功能。如果您未指定此参数，则摘要设置将由发起者的内核模式驱动程序来确定。

```yaml
Type: Boolean[]
Parameter Sets: ByTargetPortalAddress
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetPortalAddress
指定目标门户的IP地址或DNS名称。

```yaml
Type: String[]
Parameter Sets: ByTargetPortalAddress
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetPortalPortNumber
指定目标门户的TCP/IP端口号。默认情况下，端口号为3260。

```yaml
Type: UInt16[]
Parameter Sets: ByTargetPortalAddress
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算出一个最优的流量限制值。该流量限制仅适用于当前的cmdlet，而不适用于整个会话或计算机本身。

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

### -iSCSIConnection
接受一个 MSFT iSCSI 连接对象作为输入。该 MSFT iSCSI 连接对象是通过 **Get-IscsiConnection** cmdlet 获得的输出结果。

```yaml
Type: CimInstance
Parameter Sets: ByiSCSIConnection
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -iSCSISession
接受一个 MSFT iSCSI 会话对象作为输入。该 MSFT iSCSI 会话对象是通过 **Get-IscsiSession** cmdlet 获取的。

```yaml
Type: CimInstance
Parameter Sets: ByiSCSISession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -iSCSITarget
接受一个来自 Microsoft (MSFT) 的 iSCSI 目标对象作为输入。该 MSFT iSCSI 目标对象是通过 **Get-IscsiTarget** cmdlet 获取的。

```yaml
Type: CimInstance
Parameter Sets: ByiSCSITarget
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiConnection
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiSession
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiTarget
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiTargetPortal
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[TechNet上的iSCSI相关内容](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee338476(v=ws.10))

[TechNet上的存储相关信息](https://go.microsoft.com/fwlink/?linkid=191356)

[Get-IscsiConnection](./Get-IscsiConnection.md)

[Get-IscsiSession](./Get-IscsiSession.md)

[Get-IscsiTarget](./Get-IscsiTarget.md)

