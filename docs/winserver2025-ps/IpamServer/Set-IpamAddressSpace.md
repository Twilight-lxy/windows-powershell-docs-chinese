---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAddressSpace.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamaddressspace?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamAddressSpace
---

# 设置 Ipam 地址空间

## 摘要
修改 IPAM 中的地址空间。

## 语法

### 按名称查找
```
Set-IpamAddressSpace [-Name] <String[]> [-NewName <String>] [-Owner <String>] [-Description <String>]
 [-AddCustomConfiguration <String>] [-RemoveCustomConfiguration <String>]
 [-AssociatedProviderAddressSpace <String>] [-Tenant <String>] [-VmNetwork <String>]
 [-IsolationMethod <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-IpamAddressSpace -InputObject <CimInstance[]> [-NewName <String>] [-Owner <String>] [-Description <String>]
 [-AddCustomConfiguration <String>] [-RemoveCustomConfiguration <String>]
 [-AssociatedProviderAddressSpace <String>] [-Tenant <String>] [-VmNetwork <String>]
 [-IsolationMethod <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Set-IpamAddressSpace** cmdlet 用于修改 IP 地址管理 (IPAM) 中的地址空间。您可以指定要修改的地址空间，或者使用 *InputObject* 参数来指定一个需要修改的 *IpamAddressSpace* 对象。除了 *Name* 或 *InputObject* 参数外，您必须至少指定另一个可选参数。

## 示例

#### 示例 1：重命名地址空间
```
PS C:\> Set-IpamAddressSpace -Name "OneDataCenter" -NewName "MainDataCenter" -PassThru
Name                           : MainDataCenter

Type                           : ProviderAddressSpace

Owner                          :

Description                    :

AssociatedProviderAddressSpace :

Tenant                         :

VMNetwork                      :

IsolationMethod                :

Ipv4PercentageUtilized         : 66.8888888888889

Ipv6PercentageUtilized         : 0

CustomConfiguration            :
```

这个命令将名为“OneDataCenter”的地址空间重命名为“MainDataCenter”。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 2：更改客户地址空间的提供商地址空间
```
PS C:\> Get-IpamAddressSpace -Name "WoodgroveAddSpace" | Set-IpamAddressSpace -AssociatedProviderAddressSpace "MainDataCenter" -PassThru


Name                           : WoodgroveAddSpace

Type                           : CustomerAddressSpace

Owner                          :

Description                    : Equities and Mutual funds business

AssociatedProviderAddressSpace : MainDatacenter

Tenant                         : 5001

VMNetwork                      : WoodgroveBank_Network

IsolationMethod                : NVGRE

Ipv4PercentageUtilized         : 38.3838383838384

Ipv6PercentageUtilized         : 0

CustomConfiguration            :
```

该命令用于更改与客户地址空间关联的提供者地址空间。首先，使用 `Get-IpamAddressSpace` cmdlet 获取一个名为 `WoodgroveAddSpace` 的 `IpamAddressSpace` 对象；然后通过管道运算符将该对象传递给 `Set-IpamAddressSpace` cmdlet，并将名为 `MainDataCenter` 的提供者地址空间设置为该客户地址空间的新值。

## 参数

### -AddCustomConfiguration
指定用半冒号分隔的名称/值对。此参数用于指定与地址空间相关联的自定义元数据。

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

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -AssociatedProviderAddressSpace
指定与客户地址空间相关联的提供商地址空间。IPAM中的客户地址空间都属于同一个提供商地址空间。

```yaml
Type: String
Parameter Sets: (All)
Aliases: PA

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
在运行cmdlet之前会提示您进行确认。

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
指定地址空间的描述信息。

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

### -InputObject
指定传递给此 cmdlet 的输入数据。你可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

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

### -IsolationMethod
指定用于该地址空间的网络虚拟化机制。此参数的可接受值为：

- NVGRE
- IPRewrite

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

### -Name
指定一个地址空间名称的数组。该cmdlet会修改这些地址空间。

```yaml
Type: String[]
Parameter Sets: ByName
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewName
为地址空间指定一个新名称。

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

### -Owner
指定地址空间的所有者。

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

### -RemoveCustomConfiguration
指定一个由半冒号分隔的自定义字段名称字符串。该cmdlet会从地址空间中删除这些自定义字段名称。

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

### -Tenant
指定与客户地址空间关联的租户ID（以字符串形式表示）。您必须提供一个与该虚拟机网络相关联的租户ID，该虚拟机网络是通过*VmNetwork*参数指定的。

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

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算出一个最优的并发限制。这个并发限制仅适用于当前的命令（cmdlet），而不适用于整个会话或计算机本身。

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

### -VmNetwork
指定用于客户地址空间的虚拟机网络的名称。您必须指定一个与为“Tenant”参数指定的租户相关联的虚拟网络。

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

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamAddressSpace
此 cmdlet 返回一个对象，该对象代表 IPAM 中的一个地址空间。

## 备注

## 相关链接

[Get-IpamAddressSpace](./Get-IpamAddressSpace.md)

[Add-IpamAddressSpace](./Add-IpamAddressSpace.md)

[删除 Ipam 地址空间](./Remove-IpamAddressSpace.md)

