---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamBlock.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamblock?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamBlock
---

# 设置 IpamBlock

## 摘要
修改 IPAM 中的一个 IP 地址段。

## 语法

### ByKeySet
```
Set-IpamBlock [-NetworkId] <String[]> [-StartIPAddress] <IPAddress[]> [-EndIPAddress] <IPAddress[]>
 [-NewNetworkId <String>] [-NewStartIpAddress <IPAddress>] [-NewEndIpAddress <IPAddress>] [-Rir <String>]
 [-RirReceivedDate <DateTime>] [-Description <String>] [-LastAssignedDate <DateTime>] [-Owner <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InputObject（cdxml）
```
Set-IpamBlock -InputObject <CimInstance[]> [-NewNetworkId <String>] [-NewStartIpAddress <IPAddress>]
 [-NewEndIpAddress <IPAddress>] [-Rir <String>] [-RirReceivedDate <DateTime>] [-Description <String>]
 [-LastAssignedDate <DateTime>] [-Owner <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-IpamBlock` cmdlet 用于修改 IP 地址管理（IPAM）中的 IP 地址块。您可以使用 `Start IPAddress` 和 `EndIpAddress` 参数来指定地址块，或者使用 `InputObject` 参数来为该 cmdlet 提供输入数据。

如果您指定了 *NewStartIpAddress*、*NewEndIPAddress* 或 *NewNetworkId* 参数，该 cmdlet 会重置该地址块的利用率趋势信息。

## 示例

#### 示例 1：修改描述中的子 IP 地址范围
```
PS C:\> $Parent = Get-IpamBlock -NetworkId "10.0.0.0/8" -StartIPAddress 10.0.0.0 -EndIPAddress 10.255.255.255
PS C:\> Get-IpamBlock -MappingToParentBlock $Parent | Set-IpamBlock -Description "IP Blocks assigned to Site01" -PassThru
Utilization        : Under

NetworkId          : 10.12.0.0/16

StartAddress       : 10.12.0.0

EndAddress         : 10.12.255.255

Rir                :

LastAssignedDate   :

TotalAddresses     : 65536

AssignedAddresses  : 0

UtilizedAddresses  : 0

PercentageUtilized : 0

AddressCategory    : Private

Owner              :

Description        : IP Blocks assigned to Site01

RirReceivedDate    :

PercentageAssigned : 0
Utilization        : Under

NetworkId          : 10.13.0.0/16

StartAddress       : 10.13.0.0

EndAddress         : 10.13.255.255

Rir                :

LastAssignedDate   :

TotalAddresses     : 65536

AssignedAddresses  : 0

UtilizedAddresses  : 0

PercentageUtilized : 0

AddressCategory    : Private

Owner              :

Description        : IP Blocks assigned to Site01

RirReceivedDate    :

PercentageAssigned : 0
```

这个例子修改了属于某个地址块的所有子IP地址范围的描述信息。

第一个命令获取一个名为 `IpamBlock` 的对象，该对象包含了网络中的 IP 地址段（其地址范围为 10.0.0.0/8）。这个命令将 `IpamBlock` 对象存储在 `$Parent` 变量中。

第二个命令会获取存储在 `$Parent` 变量中的地址块的所有子 IP 地址范围。该命令通过使用管道运算符将这些子 IP 地址范围传递给 `Set-IpamBlock` cmdlet，并修改这些子 IP 地址范围的描述信息。

该命令包含了 *PassThru* 参数，因此会将结果显示在控制台上。

### 示例 2：修改地址块中的键属性
```
PS C:\> Get-IpamBlock -NetworkId "10.11.0.0/16" -StartIPAddress 10.11.0.0 -EndIPAddress 10.11.255.255 | Set-IpamBlock -NewNetworkId 10.13.0.0/16 -NewStartIPAddress 10.13.0.0 -NewEndIpAddress 10.13.255.255


Confirm

Changing the NetworkId, StartIPAddress, EndIPAddress of an IP address block will reset its utilization trend information

Do you want to continue? Y
```

这个命令使用 `Get-IpamBlock` 来获取网络中 ID 为 10.11.0.0/16 的 IP 地址块。该命令指定了地址块的起始地址和结束地址，并通过管道操作符将地址块传递给 `Set-IpamBlock` cmdlet。`Set-IpamBlock` cmdlet 会为该地址块设置新的网络 ID、起始地址和结束地址值。由于这个命令修改了地址块的网络 ID、起始地址和结束地址，因此它也会重置该地址块的利用率趋势数据。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。请输入一个计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -Description
为地址块指定一个描述。

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
指定 IP 地址块的结束地址。如果您指定了此参数，则必须同时指定 *StartIpAddress* 参数。

```yaml
Type: IPAddress[]
Parameter Sets: ByKeySet
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

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

### -LastAssignedDate
指定该网络规则最后一次被分配给设备的日期，该日期以 **DateTime** 对象的形式表示。要获取一个 **DateTime** 对象，可以使用 **Get-Date** cmdlet。有关更多信息，请输入 `Get-Help Get-Date`。

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
指定您想要修改的网络块的 IP 网络前缀，采用无类别域间路由（CIDR）表示法。

```yaml
Type: String[]
Parameter Sets: ByKeySet
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewEndIpAddress
为地址块的结束IP地址指定一个新值。请确保该值与您为*NewNetworkId*和*NewStartIPAddress*参数所指定的值兼容。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewNetworkId
指定一个 IP 网络前缀，采用无类别域间路由（CIDR）表示法。这是将 IP 地址块添加到 IPAM 所依据的网络的新标识信息。

请指定一个与您为 *NewStartIPAddress* 和 *NewEndIPAddress* 参数所指定的值兼容的值。

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

### -NewStartIpAddress
为地址块的起始IP地址指定一个新值。请选择一个与您为*NewNetworkId*和*NewEndIPAddress*参数指定的值兼容的值。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
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

### -Rir
用于指定公共地址所属的区域互联网注册机构（Regional Internet Registry，简称RIR）。RIR是IPAM服务器中的一个内置自定义字段，其中包含以下预定义的值：

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
指定从 Regional Internet Registry (RIR) 获取公共地址块时的日期，该日期以 **DateTime** 对象的形式表示。

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
指定 IP 地址块的起始地址。如果您指定了此参数，则必须同时指定 *EndIpAddress* 参数。

```yaml
Type: IPAddress[]
Parameter Sets: ByKeySet
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最优的节流限制（即允许同时执行的操作数量）。这个节流限制仅适用于当前的 cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果运行该cmdlet会发生什么情况。但实际上，该cmdlet并未被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamBlock
此cmdlet返回一个对象，该对象代表IPAM中的地址块对象。

## 备注

## 相关链接

[Get-IpamBlock](./Get-IpamBlock.md)

[Add-IpamBlock](./Add-IpamBlock.md)

[Remove-IpamBlock](./Remove-IpamBlock.md)

