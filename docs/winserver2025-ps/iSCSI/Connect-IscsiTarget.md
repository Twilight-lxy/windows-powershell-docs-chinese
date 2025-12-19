---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: iSCSITarget.cdxml-help.xml
Module Name: iSCSI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsi/connect-iscsitarget?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Connect-IscsiTarget
---

# 连接 Iscsi 目标设备

## 摘要
在本地 iSCSI 发起方和 iSCSI 目标设备之间建立连接。

## 语法

### ByNodeAddress（默认值）
```
Connect-IscsiTarget -NodeAddress <String> [-TargetPortalAddress <String>] [-TargetPortalPortNumber <UInt16>]
 [-InitiatorPortalAddress <String>] [-IsDataDigest <Boolean>] [-IsHeaderDigest <Boolean>]
 [-IsPersistent <Boolean>] [-ReportToPnP <Boolean>] [-AuthenticationType <String>]
 [-IsMultipathEnabled <Boolean>] [-InitiatorInstanceName <String>] [-ChapUsername <String>]
 [-ChapSecret <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByObject
```
Connect-IscsiTarget [-TargetPortalAddress <String>] [-TargetPortalPortNumber <UInt16>]
 [-InitiatorPortalAddress <String>] [-IsDataDigest <Boolean>] [-IsHeaderDigest <Boolean>]
 [-ReportToPnP <Boolean>] [-AuthenticationType <String>] [-IsMultipathEnabled <Boolean>]
 [-InitiatorInstanceName <String>] [-ChapUsername <String>] [-ChapSecret <String>] -InputObject <CimInstance[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Connect-IscsiTarget` cmdlet 用于建立与指定的 iSCSI 目标设备的连接。

## 示例

#### 示例 1：断开连接后再重新连接到 iSCSI 目标
```
The first command gets iSCSI targets by using the **Get-IscsiTarget** cmdlet.The second command gets iSCSI targets, and then stores them in the $Target variable. The third command disconnects the iSCSI target identified by its **NodeAddress** by using the **Disconnect-IscsiTarget** cmdlet. The final command connections the iSCSI target identified by its **NodeAddress**.
PS C:\> Get-IscsiTarget
IsConnected NodeAddress
----------- -----------
True iqn.1991-05.com.contoso:testiscsi-deepcore-target
PS C:\> $Target = Get-IscsiTarget
PS C:\> Disconnect-IscsiTarget -NodeAddress $Target.NodeAddress
Confirm
Are you sure you want to perform this action?
Performing operation '' on Target ''.
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): **Y**
PS C:\> Connect-IscsiTarget -NodeAddress $Target.NodeAddress
AuthenticationType      : NONE
InitiatorInstanceName   : ROOT\ISCSIPRT\0000_0
InitiatorNodeAddress    : iqn.1991-05.com.contoso:deepcore.contoso.com
InitiatorPortalAddress  :
InitiatorSideIdentifier : 400001370000
IsConnected             : True
IsDataDigest            : False
IsDiscovered            : True
IsHeaderDigest          : False
IsMultipathEnabled      : False
IsPersistent            : True
NumberOfConnections     : 1
SessionIdentifier       : fffffa800d008430-400001370000000b
TargetNodeAddress       : iqn.1991-05.com.contoso:testiscsi-deepcore-target
TargetSideIdentifier    : 0100
```

这个示例首先连接到一个 iSCSI 目标设备，收集有关该目标设备的信息，并将这些信息存储在一个变量中；随后断开连接，再使用该 cmdlet 重新建立连接。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -AuthenticationType
指定在登录目标系统时使用的认证类型。该参数的可接受值包括：

- NONE
- ONEWAYCHAP
- MUTUALCHAP

默认值为 `None`。身份验证类型必须使用大写字母表示。

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

### -ChapSecret
指定在建立通过CHAP（Challenge-Handshake Authentication）进行身份验证的连接时所使用的CHAP密钥。

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

### -ChapUsername
指定在通过相互CHAP（Mutual CHAP）身份验证建立连接时使用的用户名。

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

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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
指定 iSCSI 启动器服务用于向目标门户发送 **SendTargets** 请求的启动器实例的名称。如果未指定实例名称，iSCSI 启动器服务会自行选择相应的启动器实例。

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
指定与门户相关联的 IP 地址或 DNS 名称。

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
指定要传递给此cmdlet的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: ByObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IsDataDigest
该参数用于指示当发起者登录目标门户时，此 cmdlet 是否启用数据摘要功能。如果您未指定此参数，则摘要功能的设置将由发起者的内核模式驱动程序决定。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsHeaderDigest
该参数用于指示当发起者登录目标门户时，此cmdlet是否启用头部摘要功能。如果您未指定此参数，则摘要功能的设置将由发起者的内核模式驱动程序决定。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsMultipathEnabled
该指示用于显示发起者是否启用了多路径输入/输出（Multipath I/O，简称MPIO），以及在登录目标门户时是否使用了该功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsPersistent
指示每次重启后会自动连接会话吗？

```yaml
Type: Boolean
Parameter Sets: ByNodeAddress
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NodeAddress
指定已发现目标的IQN（Identity Qualified Name）。

```yaml
Type: String
Parameter Sets: ByNodeAddress
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReportToPnP
指示该操作是否会被报告给菲律宾国家警察局（PNP）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetPortalAddress
指定目标门户的IP地址或DNS名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: TA

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetPortalPortNumber
指定目标门户的TCP/IP端口号。默认情况下，端口号为3260。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时建立的、用于运行该cmdlet的操作的最大数量。如果省略了这个参数或输入了`0`，那么Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算出一个最优的速率限制（throttle limit）。这个速率限制仅适用于当前的cmdlet，而不适用于整个会话或计算机本身。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiSession
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[TechNet上的iSCSI相关内容](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee338476(v=ws.10))

[TechNet上的存储相关内容](https://go.microsoft.com/fwlink/?linkid=191356)

[ Disconnect-IscsiTarget](./Disconnect-IscsiTarget.md)

[Get-IscsiTarget](./Get-IscsiTarget.md)

