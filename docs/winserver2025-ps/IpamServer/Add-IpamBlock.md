---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamBlock.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/add-ipamblock?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-IpamBlock
---

# Add-IpamBlock

## 摘要
将一个IP地址段添加到IPAM中。

## 语法

```
Add-IpamBlock [-NetworkId] <String> [[-StartIPAddress] <IPAddress>] [[-EndIPAddress] <IPAddress>]
 [-Rir <String>] [-RirReceivedDate <DateTime>] [-Description <String>] [-LastAssignedDate <DateTime>]
 [-Owner <String>] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
**Add-IpamBlock** cmdlet 用于将一个 IP 地址块添加到 IP 地址管理（IPAM）系统中。请使用 *NetworkID* 参数指定要从中添加该 IP 地址块的网络。如果您添加的地址块属于公共地址类别，那么必须指定 *Rir* 参数；对于私有地址块来说，*Rir* 参数是可选的。

## 示例

#### 示例 1：添加一个 IPv4 私有地址段
```
PS C:\> Add-IpamBlock -NetworkId "10.0.0.0/8" -Description "IP block for Contoso" -PassThru


Utilization        : Under

NetworkId          : 10.0.0.0/8

StartAddress       : 10.0.0.0

EndAddress         : 10.255.255.255

Rir                :

LastAssignedDate   :

TotalAddresses     : 16777216

AssignedAddresses  : 2440

UtilizedAddresses  : 732

PercentageUtilized : 30

AddressCategory    : Private

Owner              :

Description        : IP block for Contoso

RirReceivedDate    :

PercentageAssigned : 1.454353
```

此命令用于向 IPAM 服务器添加一个 IPv4 私有地址块。该命令使用网络 ID 为 10.0.0.0/8 的第一个地址和最后一个地址作为该地址块的起始地址和结束地址。同时，该命令包含了 *PassThru* 参数，因此会将执行结果显示在控制台中。

### 示例 2：添加一个公共地址块
```
PS C:\> Add-IpamBlock -NetworkId "206.73.118.0/24" -Rir "APNIC" -PassThru


Utilization        : Under

NetworkId          : 206.73.118.0/24

StartAddress       : 206.73.118.0

EndAddress         : 206.73.118.255

Rir                : APNIC

LastAssignedDate   :

TotalAddresses     : 256

AssignedAddresses  : 0

UtilizedAddresses  : 0

PercentageUtilized : 0

AddressCategory    : Public

Owner              :

Description        :

RirReceivedDate    :

PercentageAssigned : 0
```

此命令用于向 IPAM 服务器添加一个公共地址段。如果您要添加的地址段的类别为“Public”，则必须指定 **Rir** 参数。

### 示例 3：添加一个 IPv6 地址块
```
PS C:\> Add-IpamBlock -NetworkId 2001:DB8:ff00::/120 -PassThru


Utilization        : Under

NetworkId          : 2001:db8:ff00::/120

StartAddress       : 2001:db8:ff00::

EndAddress         : 2001:db8:ff00::ff

Rir                :

LastAssignedDate   :

TotalAddresses     : 256

AssignedAddresses  : 0

UtilizedAddresses  : 0

PercentageUtilized : 0

AddressCategory    : Global

Owner              :

Description        :

RirReceivedDate    :

PercentageAssigned : 0
```

此命令向 IPAM 服务器添加一个 IPv6 地址段。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 获得的会话对象）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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

### -Description
为地址块指定一个描述性文字。

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

### -EndIPAddress
用于指定 IP 地址块的结束地址。如果不指定此参数，cmdlet 将使用为 *NetworkId* 参数指定的网络的最后一个 IP 地址。如果指定了此参数，则必须同时指定 *StartIpAddress* 参数。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LastAssignedDate
指定该数据块最后一次被分配到网络中的设备的日期，该日期以 **DateTime** 对象的形式表示。要获取一个 **DateTime** 对象，可以使用 **Get-Date** cmdlet。有关更多信息，请输入 `Get-Help Get-Date`。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkId
指定一个 IP 网络前缀，采用无类别域间路由（CIDR）表示法。该网络是用于将 IP 地址块添加到 IPAM 服务器中的来源网络。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Owner
指定 IP 地址块的拥有者。

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

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Rir
指定用于公共地址的区域互联网注册机构（RIR）。RIR是IPAM服务器中的一个内置自定义字段，其中包含以下预设值：

- AFRINIC
- APNIC
- ARIN
- LACNIC
- RIPE

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

### -RirReceivedDate
指定从区域互联网注册机构（RIR）获取公共地址块的日期，该日期以 **DateTime** 对象的形式表示。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartIPAddress
指定 IP 地址块的起始地址。如果您不指定此参数，cmdlet 将使用您为 *NetworkId* 参数指定的网络中的第一个地址。如果您指定了此参数，则必须同时指定 *EndIpAddress* 参数。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算一个最优的并发限制。该并发限制仅适用于当前运行的命令，而不适用于整个会话或整个计算机。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-IpamBlock](./Get-IpamBlock.md)

[Set-IpamBlock](./Set-IpamBlock.md)

[Remove-IpamBlock](./Remove-IpamBlock.md)

