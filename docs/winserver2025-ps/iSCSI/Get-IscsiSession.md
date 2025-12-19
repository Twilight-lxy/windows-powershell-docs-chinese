---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: iSCSISession.cdxml-help.xml
Module Name: iSCSI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsi/get-iscsisession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IscsiSession
---

# Get-IscsiSession

## 摘要
检索有关已建立的iSCSI会话的信息。

## 语法

### 按会话标识符（默认值）
```
Get-IscsiSession [<CommonParameters>]
```

### 根据目标方标识符（ByTargetSideIdentifier）
```
Get-IscsiSession [-SessionIdentifier <String[]>] [-TargetSideIdentifier <String[]>]
 [-NumberOfConnections <UInt32[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByInitiatorSideIdentifier
```
Get-IscsiSession [-InitiatorSideIdentifier <String[]>] [-NumberOfConnections <UInt32[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByiSCSITarget
```
Get-IscsiSession [-NumberOfConnections <UInt32[]>] [-IscsiTarget <CimInstance>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByInitiatorPort
```
Get-IscsiSession [-NumberOfConnections <UInt32[]>] [-InitiatorPort <CimInstance>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByiSCSITargetPortal
```
Get-IscsiSession [-NumberOfConnections <UInt32[]>] [-IscsiTargetPortal <CimInstance>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 按磁盘划分
```
Get-IscsiSession [-NumberOfConnections <UInt32[]>] [-Disk <CimInstance>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByiSCSIConnection
```
Get-IscsiSession [-NumberOfConnections <UInt32[]>] [-IscsiConnection <CimInstance>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-IscsiSession` cmdlet 可以返回有关 iSCSI 会话的信息。

iSCSI会话与磁盘对象之间存在关联。可以通过运行以下命令来返回通过特定iSCSI会话连接的所有磁盘：

请帮我将以下Markdown内容转换为中文：

```
PS C:\> `Get-iSCSISession | Get-Disk`
```

## 示例

### 示例 1：获取有关 iSCSI 会话的信息
```
PS C:\> Get-IscsiSession
AuthenticationType      : NONE
InitiatorInstanceName   : ROOT\ISCSIPRT\0000_0
InitiatorNodeAddress    : iqn.1991-05.com.microsoft:deepcore.contoso.com
InitiatorPortalAddress  :
InitiatorSideIdentifier : 400001370001
IsConnected             : True
IsDataDigest            : False
IsDiscovered            : True
IsHeaderDigest          : False
IsMultipathEnabled      : False
IsPersistent            : True
NumberOfConnections     : 1
SessionIdentifier       : fffffa800d008430-4000013700000001
TargetNodeAddress       : iqn.1991-05.com.contoso:testiscsi-deepcore-target
TargetSideIdentifier    : 0200

AuthenticationType      : NONE
InitiatorInstanceName   : ROOT\ISCSIPRT\0000_0
InitiatorNodeAddress    : iqn.1991-05.com.contoso:deepcore.contoso.com
InitiatorPortalAddress  :
InitiatorSideIdentifier : 400001370004
IsConnected             : True
IsDataDigest            : False
IsDiscovered            : True
IsHeaderDigest          : False
IsMultipathEnabled      : False
IsPersistent            : True
NumberOfConnections     : 1
SessionIdentifier       : fffffa800d008430-4000013700000002
TargetNodeAddress       : iqn.1991-05.com.contoso:testiscsi-deepcore-target
TargetSideIdentifier    : 0100

AuthenticationType      : NONE
InitiatorInstanceName   : ROOT\ISCSIPRT\0000_0
InitiatorNodeAddress    : iqn.1991-05.com.contoso:deepcore.contoso.com
InitiatorPortalAddress  :
InitiatorSideIdentifier : 400001370002
IsConnected             : True
IsDataDigest            : False
IsDiscovered            : True
IsHeaderDigest          : False
IsMultipathEnabled      : False
IsPersistent            : True
NumberOfConnections     : 1
SessionIdentifier       : fffffa800d008430-4000013700000003
TargetNodeAddress       : iqn.1991-05.com.contoso:testiscsi-deepcore-target
TargetSideIdentifier    : 0300
```

此命令会返回有关 iSCSI 会话的信息。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job` cmdlets系列命令；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: ByTargetSideIdentifier, ByInitiatorSideIdentifier, ByiSCSITarget, ByInitiatorPort, ByiSCSITargetPortal, ByDisk, ByiSCSIConnection
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: ByTargetSideIdentifier, ByInitiatorSideIdentifier, ByiSCSITarget, ByInitiatorPort, ByiSCSITargetPortal, ByDisk, ByiSCSIConnection
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Disk
接受一个 MSFT 磁盘对象作为输入。该 MSFT 磁盘对象是通过 **Get-Disk** cmdlet 获得的。

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
接受一个 MSFT 发起者端口对象作为输入参数。该 MSFT 发起者端口对象是通过 **Get-InitiatorPort** cmdlet 命令获取的。

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

### -InitiatorSideIdentifier
指定发起方识别符。

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

### -IscsiConnection
该函数接受一个来自 Microsoft (MSFT) 的 iSCSI 连接对象作为输入。这个 MSFT iSCSI 连接对象是通过 **Get-IscsiConnection** cmdlet 获取的。

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

### -IscsiTarget
接受一个 MSFT iSCSI 目标对象作为输入。该 MSFT iSCSI 目标对象是通过 **Get-IscsiTarget** cmdlet 获得的输出结果。

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

### -IscsiTargetPortal
接受一个 MSFT iSCSI 目标门户对象作为输入。该 MSFT iSCSI 目标门户对象是通过 **Get-IscsiTargetPortal** cmdlet 获得的输出结果。

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

### -NumberOfConnections
指定连接的数量。

```yaml
Type: UInt32[]
Parameter Sets: ByTargetSideIdentifier, ByInitiatorSideIdentifier, ByiSCSITarget, ByInitiatorPort, ByiSCSITargetPortal, ByDisk, ByiSCSIConnection
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SessionIdentifier
指定会话标识符。

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

### -TargetSideIdentifier
指定目标方的标识符。

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
该参数用于指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: ByTargetSideIdentifier, ByInitiatorSideIdentifier, ByiSCSITarget, ByInitiatorPort, ByiSCSITargetPortal, ByDisk, ByiSCSIConnection
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_DISK
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_InitiatorPort
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiConnection
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiTarget
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiTargetPortal
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiSession
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[TechNet上的iSCSI相关内容](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee338476(v=ws.10))

[TechNet上的存储相关内容](https://go.microsoft.com/fwlink/?linkid=191356)

[Get-IscsiConnection](./Get-IscsiConnection.md)

[Get-IscsiTarget](./Get-IscsiTarget.md)

[Get-IscsiTargetPortal](./Get-IscsiTargetPortal.md)

