---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamBlock.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/remove-ipamblock?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IpamBlock
---

# 移除 IPAM 阻塞（Remove-IpamBlock）

## 摘要
从 IPAM 中删除一个地址块。

## 语法

### ByKeySet
```
Remove-IpamBlock [-NetworkId] <String[]> [-StartIPAddress] <IPAddress[]> [-EndIPAddress] <IPAddress[]>
 [-DeleteAssociatedSubBlocks] [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Remove-IpamBlock -InputObject <CimInstance[]> [-DeleteAssociatedSubBlocks] [-Force]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-IpamBlock` cmdlet 用于从 IP 地址管理（IPAM）中删除一个 IP 地址块。您可以使用 `StartIPAddress` 和 `EndIPAddress` 参数来指定地址块，或者使用 `InputObject` 参数来提供该 cmdlet 需要处理的输入数据。此外，您还可以通过设置 `DeleteAssociatedSubBlocks` 参数来移除与该地址块关联的所有子 IP 地址范围。当您删除一个地址块时，IPAM 会重新映射所有子网，并取消之前将该地址块与某些子网之间的关联。

## 示例

### 示例 1：删除一个 IP 地址段
```
PS C:\> Get-IpamBlock -NetworkId "10.15.0.0/16" -StartIPAddress 10.15.0.0 -EndIPAddress 10.15.255.255 | Remove-IpamBlock
Confirm

Deleting IP address block with NetworkId 10.15.0.0/16 from IPAM. Deleting the block may move the currently mapped IP address ranges within this block to Unmapped address space.Do you want to continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y
```

这个命令会从网络中移除ID为10.15.0.0/8/16的IP地址段。该命令指定了该地址段的起始地址和结束地址。

### 示例 2：删除所有属于某个地址块的子 IP 地址范围
```
PS C:\> Get-IpamBlock -NetworkId "10.0.0.0/8" -StartIPAddress 10.0.0.0 -EndIPAddress 10.255.255.255 | Remove-IpamBlock -DeleteAssociatedSubBlocks
Confirm

This will permanently delete the given IP Block with NetworkId 10.0.0.0/8 from IPAM. Deleting the block may move the currently mapped IP address ranges within this block to Unmapped address space. Any sub-blocks associated with the given block will also be deleted. Do you want to continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y
```

该命令会从ID为10.0.0.0/8的网络中移除所有属于该地址块的子IP地址范围。命令指定了该地址块的起始地址和结束地址。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中执行其他操作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -DeleteAssociatedSubBlocks
表示该cmdlet会删除属于该地址块的子IP地址范围。

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

### -EndIPAddress
指定一个包含IP地址块结束地址的数组。

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

### -Force
强制命令运行，而无需询问用户确认。

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

### -InputObject
指定该cmdlet的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

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

### -NetworkId
指定要删除的网络块的 IP 网络前缀，采用无类别域间路由（CIDR）表示法。

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

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -StartIPAddress
指定一个包含IP地址块起始地址的数组。

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
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值（即并发操作的最大数量）。这个限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
此cmdlet返回一个对象，该对象表示IPAM中的地址块。

## 备注

## 相关链接

[Get-IpamBlock](./Get-IpamBlock.md)

[Set-IpamBlock](./Set-IpamBlock.md)

[Add-IpamBlock](./Add-IpamBlock.md)

