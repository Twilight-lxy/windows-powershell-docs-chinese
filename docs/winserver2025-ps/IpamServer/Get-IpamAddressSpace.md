---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAddressSpace.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamaddressspace?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamAddressSpace
---

# 获取 Ipam 地址空间

## 摘要
获取IPAM中的地址空间信息。

## 语法

### 按名称查找
```
Get-IpamAddressSpace [[-Name] <String[]>] [[-Type] <AddressSpaceType[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByMapping
```
Get-IpamAddressSpace -MappingToProviderAddressSpace <String[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
**Get-IpamAddressSpace** 这个 cmdlet 可以用来获取 IP 地址管理（IPAM）中的地址空间信息。你可以指定 *MappingToProviderAddressSpace* 参数，以获取属于某个提供者地址组的所有客户地址空间；IPAM 中的客户地址空间都属于同一个提供者地址空间。你还可以使用 *Name* 参数来筛选出名称与指定值相匹配的地址空间，或者使用 *Type* 参数来筛选出类型与指定值相匹配的地址空间。对于 *Name* 参数，你可以使用通配符来匹配具有特定前缀或后缀的所有地址空间。如果你不指定任何参数，该 cmdlet 会获取 IPAM 中所有的地址空间信息。

## 示例

#### 示例 1：获取所有地址空间
```
PS C:\> Get-IpamAddressSpace
```

这个命令可以获取IPAM中的所有地址空间信息。

### 示例 2：获取地址空间
```
PS C:\> Get-IpamAddressSpace -Name "ContosoMusic"
Name                           : ContosoMusic

Type                           : CustomerAddressSpace

Owner                          :

Description                    : Music Mp3

AssociatedProviderAddressSpace : MainDatacenter

Tenant                         : 4001

VMNetwork                      : ContosoMusic_Network

IsolationMethod                : NVGRE

Ipv4PercentageUtilized         : 62.0805369127517

Ipv6PercentageUtilized         : 0

CustomConfiguration            :
```

这个命令用于获取名为“ContosoMusic”的地址空间。

### 示例 3：获取所有映射到提供商地址空间的客户地址空间
```
PS C:\> Get-IpamAddressSpace -MappingToProviderAddressSpace "MainDataCenter"
Name                           : TreyResearch

Type                           : CustomerAddressSpace

Owner                          :

Description                    : A research and design company

AssociatedProviderAddressSpace : MainDatacenter

Tenant                         : 1001

VMNetwork                      : Trey Research_Network

IsolationMethod                : NVGRE

Ipv4PercentageUtilized         : 15.1515151515152

Ipv6PercentageUtilized         : 0

CustomConfiguration            :
Name                           : ContosoMusic

Type                           : CustomerAddressSpace

Owner                          :

Description                    : Music Mp3

AssociatedProviderAddressSpace : MainDatacenter

Tenant                         : 4001

VMNetwork                      : ContosoTunes_Network

IsolationMethod                : NVGRE

Ipv4PercentageUtilized         : 62.0805369127517

Ipv6PercentageUtilized         : 0

CustomConfiguration            :
```

此命令获取所有属于名为“MainDataCenter”的提供者地址空间的客户地址空间。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在该会话中操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

### -MappingToProviderAddressSpace
指定一个提供商地址空间名称数组。该cmdlet会获取所有属于这些提供商地址空间的客户地址空间。

```yaml
Type: String[]
Parameter Sets: ByMapping
Aliases: PA

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个用于地址空间的名称数组。该cmdlet会获取所有与您指定的名称相匹配的地址空间。

```yaml
Type: String[]
Parameter Sets: ByName
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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

### -Type
指定一个地址空间类型数组。

此参数的可接受值为：

- ProviderAddressSpace
- CustomerAddressSpace

```yaml
Type: AddressSpaceType[]
Parameter Sets: ByName
Aliases:
Accepted values: ProviderAddressSpace, CustomerAddressSpace

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

## 输出

### IpamAddressSpace
This cmdlet returns an object that represents address space information, including the type of address space which can be CustomerAddressSpace or ProviderAddressSpace.

## 备注

## 相关链接

[Add-IpamAddressSpace](./Add-IpamAddressSpace.md)

[Set-IpamAddressSpace](./Set-IpamAddressSpace.md)

[Remove-IpamAddressSpace](./Remove-IpamAddressSpace.md)

