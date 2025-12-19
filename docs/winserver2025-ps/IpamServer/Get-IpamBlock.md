---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamBlock.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamblock?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamBlock
---

# Get-IpamBlock

## 摘要
从 IPAM 获取一组地址块。

## 语法

### ByNetworkId
```
Get-IpamBlock -NetworkId <String[]> -StartIPAddress <IPAddress[]> -EndIPAddress <IPAddress[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 按地址族分类
```
Get-IpamBlock [-AddressFamily] <AddressFamily[]> [[-AddressCategory] <AddressCategory[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByParent
```
Get-IpamBlock -MappingToParentBlock <CimInstance> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述
**Get-IpamBlock** cmdlet 用于从 IP 地址管理（IPAM）系统中获取一组 IP 地址块。可以通过指定 *AddressFamily* 参数来获取特定地址族的 IP 地址；通过指定 *NetworkId*、*StartIPAddress* 和 *EndIPAddress* 参数来获取特定网络的 IP 地址块；此外，还可以通过指定 *MappingToParentBlock* 参数来获取属于某个 IP 地址块的所有子 IP 地址范围。

## 示例

### 示例 1：获取所有私有 IPv4 地址块
```
PS C:\> Get-IpamBlock -AddressFamily IPv4 -AddressCategory Private | Format-List NetworkId, StartIPAddress, EndIPAddress
NetworkId      : 10.0.0.0/8

StartIPAddress : 10.0.0.0

EndIPAddress   : 10.255.255.255
```

此命令用于获取 IPAM 中所有的私有 IPv4 地址块。该命令仅返回地址块层次结构中的顶级块信息，并使用 **Format-List** cmdlet 将输出结果以表格的形式显示。如需更多详细信息，请输入 `Get-Help Format-Table`。

### 示例 2：使用网络 ID 获取地址块
```
PS C:\> Get-IpamBlock -NetworkId "10.0.0.0/8" -StartIPAddress 10.0.0.0 -EndIPAddress 10.255.255.255
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

Description        : IP block to be used for Region1

RirReceivedDate    :

PercentageAssigned : 0.01454353
```

这个命令从网络中获取ID为10.0.0.0/8的IP地址段。该命令指定了该地址段的起始地址和结束地址。

### 示例 3：将子 IP 地址范围映射到某个地址块
```
PS C:\> $Parent = Get-IpamBlock -NetworkId "10.0.0.0/8" -StartIPAddress 10.0.0.0 -EndIPAddress 10.255.255.255PS
C:\> Get-IpamBlock -MappingToParentBlock $Parent
Utilization        : Under

NetworkId          : 10.11.0.0/16

StartAddress       : 10.11.0.0

EndAddress         : 10.11.255.255

Rir                :

LastAssignedDate   :

TotalAddresses     : 65536

AssignedAddresses  : 200

UtilizedAddresses  : 90

PercentageUtilized : 45

AddressCategory    : Private

Owner              :

Description        : IP block to be used for Region1

RirReceivedDate    :

PercentageAssigned : 0.3051758
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

Description        : IP block to be used for Region1

RirReceivedDate    :

PercentageAssigned : 0
```

这个示例可以获取一个地址块中所有的子IP地址范围。

第一个命令获取一个名为 `IpamBlock` 的对象，该对象包含了网络中 IP 地址块的信息（该地址块的 ID 为 10.0.0.0/8）。此命令将 `IpamBlock` 对象存储在 `$Parent` 变量中。

第二个命令会获取存储在 $Parent 变量中的地址块的所有子 IP 地址范围。

## 参数

### -AddressCategory
指定一个IP地址类别数组。如果指定了此参数，则必须同时指定*AddressFamily*参数。

此参数的可接受值为：

- Public
- Private

```yaml
Type: AddressCategory[]
Parameter Sets: ByAddressFamily
Aliases:
Accepted values: Public, Private, Global

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddressFamily
指定一个包含IP地址地址族的数组。

此参数的可接受值为：

- IPv4
- IPv6

```yaml
Type: AddressFamily[]
Parameter Sets: ByAddressFamily
Aliases:
Accepted values: IPv4, IPv6

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -EndIPAddress
指定一个包含IP地址块结束地址的数组。

```yaml
Type: IPAddress[]
Parameter Sets: ByNetworkId
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MappingToParentBlock
指定一个 **IpamBlock** 对象。该对象表示父地址块。此 cmdlet 会获取该父地址块下的所有子 IP 地址范围。

```yaml
Type: CimInstance
Parameter Sets: ByParent
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -NetworkId
使用无类别域间路由（CIDR）表示法指定一个IP网络前缀。

```yaml
Type: String[]
Parameter Sets: ByNetworkId
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartIPAddress
指定一组用于IP地址块的起始地址数组。

```yaml
Type: IPAddress[]
Parameter Sets: ByNetworkId
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的最大操作数。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Set-IpamBlock](./Set-IpamBlock.md)

[Add-IpamBlock](./Add-IpamBlock.md)

[Remove-IpamBlock](./Remove-IpamBlock.md)

