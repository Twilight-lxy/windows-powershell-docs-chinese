---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DtcNetworkSettingTask_v1.0.cdxml-help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/set-dtcnetworksetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DtcNetworkSetting
---

# Set-DtcNetworkSetting

## 摘要
修改 DTC 实例的网络和安全配置。

## 语法

### NetworkSettings
```
Set-DtcNetworkSetting [-DtcName <String>] [-InboundTransactionsEnabled <Boolean>]
 [-OutboundTransactionsEnabled <Boolean>] [-RemoteClientAccessEnabled <Boolean>]
 [-RemoteAdministrationAccessEnabled <Boolean>] [-XATransactionsEnabled <Boolean>]
 [-LUTransactionsEnabled <Boolean>] [-AuthenticationLevel <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### DisableNetwork
```
Set-DtcNetworkSetting [-DtcName <String>] [-DisableNetworkAccess] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DtcNetworkSetting` cmdlet 用于修改由 `DtcName` 参数指定的分布式事务协调器（DTC）实例的网络和安全配置。此外，该 cmdlet 还会重启该 DTC 实例。

## 示例

### 示例 1：修改网络和安全设置
```
PS C:\> Set-DtcNetworkSetting -DtcName "Local" -AuthenticationLevel "Incoming" -InboundTransactionsEnabled $False
PS C:\> Get-DtcNetworkSetting -DtcName "Local"
__GENUS                           : 2
__CLASS                           : DtcNetworkSettings
__SUPERCLASS                      :
__DYNASTY                         : DtcNetworkSettings
__RELPATH                         :
__PROPERTY_COUNT                  : 7
__DERIVATION                      : {}
__SERVER                          :
__NAMESPACE                       :
__PATH                            :
AuthenticationLevel               : Mutual
InboundTransactionsEnabled        : True
LUTransactionsEnabled             : True
OutboundTransactionsEnabled       : True
RemoteAdministrationAccessEnabled : True
RemoteClientAccessEnabled         : True
XATransactionsEnabled             : True
```

第一个命令修改了本地DTC实例的DTC网络和安全设置。第二个命令用于验证这些更改是否已经生效。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -AuthenticationLevel
将DTC实例的网络认证级别设置为NoAuth、Incoming或Mutual。

```yaml
Type: String
Parameter Sets: NetworkSettings
Aliases:
Accepted values: NoAuth, Incoming, Mutual

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet将在本地计算机的当前会话中运行。

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

### -DisableNetworkAccess
指定是否要禁用 DTC 实例的网络访问功能。

```yaml
Type: SwitchParameter
Parameter Sets: DisableNetwork
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DtcName
用于指定一个DTC（分布式事务协调器）实例。如果您不指定此参数，或者指定的值为“Local”，则此cmdlet会修改本地的DTC实例。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -InboundTransactionsEnabled
指示是否启用对 DTC 实例的入站事务（inbound transactions）。

```yaml
Type: Boolean
Parameter Sets: NetworkSettings
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LUTransactionsEnabled
指示是否在DTC实例中启用LU（Linear Unit）交易功能。

```yaml
Type: Boolean
Parameter Sets: NetworkSettings
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OutboundTransactionsEnabled
表示是否启用来自 DTC 实例的出站交易。

```yaml
Type: Boolean
Parameter Sets: NetworkSettings
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoteAdministrationAccessEnabled
用于指示是否为 DTC 实例启用远程管理访问功能。

```yaml
Type: Boolean
Parameter Sets: NetworkSettings
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoteClientAccessEnabled
指示是否为 DTC 实例启用远程客户端访问功能。

```yaml
Type: Boolean
Parameter Sets: NetworkSettings
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最优限制值。这个限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

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

### -XATransactionsEnabled
表示是否在 DTC 实例中启用 XA 事务。

```yaml
Type: Boolean
Parameter Sets: NetworkSettings
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-DtcNetworkSetting](./Get-DtcNetworkSetting.md)

