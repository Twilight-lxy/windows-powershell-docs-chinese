---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: iSCSIConnection.cdxml-help.xml
Module Name: iSCSI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsi/get-iscsiconnection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IscsiConnection
---

# Get-IscsiConnection

## 摘要
获取有关已连接的 iSCSI 发起者连接的信息。

## 语法

### ByConnectionIdentifier（默认值）
```
Get-IscsiConnection [-ConnectionIdentifier <String[]>] [-InitiatorPortalPortNumber <UInt16[]>]
 [-InititorIPAdressListNumber <UInt16[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByInitiatorSideIdentifier
```
Get-IscsiConnection [-InitiatorSideIdentifier <String[]>] [-InitiatorPortalPortNumber <UInt16[]>]
 [-InititorIPAdressListNumber <UInt16[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### 根据目标方标识符（ByTargetSideIdentifier）
```
Get-IscsiConnection [-TargetSideIdentifier <String[]>] [-InitiatorPortalPortNumber <UInt16[]>]
 [-InititorIPAdressListNumber <UInt16[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByInitiatorPortalAddress
```
Get-IscsiConnection [-InitiatorPortalAddress <String[]>] [-InitiatorPortalPortNumber <UInt16[]>]
 [-InititorIPAdressListNumber <UInt16[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByiSCSITarget
```
Get-IscsiConnection [-InitiatorPortalPortNumber <UInt16[]>] [-InititorIPAdressListNumber <UInt16[]>]
 [-IscsiTarget <CimInstance>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByInitiatorPort
```
Get-IscsiConnection [-InitiatorPortalPortNumber <UInt16[]>] [-InititorIPAdressListNumber <UInt16[]>]
 [-InitiatorPort <CimInstance>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByiSCSISession
```
Get-IscsiConnection [-InitiatorPortalPortNumber <UInt16[]>] [-InititorIPAdressListNumber <UInt16[]>]
 [-IscsiSession <CimInstance>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByiSCSITargetPortal
```
Get-IscsiConnection [-InitiatorPortalPortNumber <UInt16[]>] [-InititorIPAdressListNumber <UInt16[]>]
 [-iSCSITargetPortal <CimInstance>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### 按磁盘分类
```
Get-IscsiConnection [-InitiatorPortalPortNumber <UInt16[]>] [-InititorIPAdressListNumber <UInt16[]>]
 [-Disk <CimInstance>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-IscsiConnection` cmdlet 可以返回有关当前活动的 iSCSI 发起者连接的信息。

## 示例

### 示例 1：显示有关已连接的 iSCI 目标设备的信息
```
PS C:\> Get-IscsiConnection
ConnectionIdentifier : fffffa8005313020-2
InitiatorNodeAddress : 0.0.0.0
InitiatorPortNumber  : 41458
TargetNodeAddress    : 10.121.235.126
TargetPortNumber     : 3260
```

该命令显示了从这个连接到iSCSI目标的cmdlet返回的信息。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -ConnectionIdentifier
指定 iSCSI 会话的连接标识符。

```yaml
Type: String[]
Parameter Sets: ByConnectionIdentifier
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Disk
接受一个来自 Microsoft 的磁盘对象作为输入。该磁盘对象是通过 **Get-Disk** cmdlet 获得的。

```yaml
Type: CimInstance
Parameter Sets: ByDisk
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -InitiatorPort
该函数以一个 MSFT 初始端口对象作为输入参数。这个 MSFT 初始端口对象是通过 **Get-InitiatorPort** cmdlet 获得的。

```yaml
Type: CimInstance
Parameter Sets: ByInitiatorPort
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -InitiatorPortalAddress
指定与门户相关联的IP地址或DNS名称。

```yaml
Type: String[]
Parameter Sets: ByInitiatorPortalAddress
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InitiatorPortalPortNumber
指定发起者门户的TCP/IP端口号。

```yaml
Type: UInt16[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InitiatorSideIdentifier
指定发起方标识符。

```yaml
Type: String[]
Parameter Sets: ByInitiatorSideIdentifier
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InititorIPAdressListNumber
指定用于索引发起者 IP 地址列表的位置。

```yaml
Type: UInt16[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IscsiSession
接受一个 MSFT iSCSI 会话对象作为输入。该 MSFT iSCSI 会话对象是通过 **Get-IscsiSession** cmdlet 获得的输出结果。

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

### -IscsiTarget
该功能接受一个来自 Microsoft (MSFT) 的 iSCSI 目标对象作为输入。这个 MSFT iSCSI 目标对象是通过 **Get-IscsiTarget** cmdlet 获取的。

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

### -TargetSideIdentifier
指定目标端的标识符。

```yaml
Type: String[]
Parameter Sets: ByTargetSideIdentifier
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前执行的 cmdlet，而不适用于整个会话或整个计算机。

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

### -iSCSITargetPortal
该函数接受一个来自 Microsoft (MSFT) 的 iSCSI 目标门户（target portal）CIM 对象作为输入。这个 MSFT iSCSI 目标门户 CIM 对象是通过 **Get-IscsiTargetPortal** cmdlet 获取的。

```yaml
Type: CimInstance
Parameter Sets: ByiSCSITargetPortal
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_DISK
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_InitiatorPort
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiSession
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiTarget
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiTargetPortal
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_iSCSIConnection
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[TechNet上的iSCSI相关内容](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee338476(v=ws.10))

[TechNet上的存储相关内容](https://go.microsoft.com/fwlink/?linkid=191356)

[Get-IscsiSession](./Get-IscsiSession.md)

[Get-IscsiTarget](./Get-IscsiTarget.md)

[Get-IscsiTargetPortal](./Get-IscsiTargetPortal.md)

