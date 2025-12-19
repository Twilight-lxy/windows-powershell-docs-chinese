---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamCapabilities.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/disable-ipamcapability?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-IpamCapability
---

# 禁用IPAM功能

## 摘要
禁用 IPAM 中的一项可选功能。

## 语法

```
Disable-IpamCapability [-Capability] <Capability> [-Force] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-Ipam Capability` cmdlet 用于禁用 Internet 协议地址管理（IPAM）中的某个可选功能。请指定要禁用的功能的名称。使用 `Enable-Ipam Capability` cmdlet 可以重新启用 IPAM 中的该可选功能。

目前，IP地址跟踪是唯一可用的可选功能。当您运行此cmdlet时，IPAM将停止收集任何新的审计数据，但会保留之前收集的数据。

## 示例

### 示例 1：在 IPAM 中禁用 IP 地址跟踪功能
```
PS C:\> Disable-IpamCapability -Capability IpAddressTracking
Confirm

Disabling IpAddressTracking. Do you want to continue?.

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): y

PS C:\> Get-IpamCapability
Name                                                        Status

----                                                        ------

IpAddressTracking                                           Disabled
```

此命令会禁用 IPAM 中的 IP 地址跟踪功能。IPAM 之前收集的数据将会被保留。运行此命令后，IPAM 将停止收集任何新的审计数据。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -Capability
指定一个可选的 IPAM 功能的名称。此 cmdlet 会禁用该可选的 IPAM 功能。目前，IpAddressTracking 是该参数的唯一有效值。

```yaml
Type: Capability
Parameter Sets: (All)
Aliases:
Accepted values: IpAddressTracking

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如使用[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Force
强制命令运行，而无需请求用户确认。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行会发生的后果。但实际上，这个cmdlet并没有被执行。

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

### IpamCapability
此 cmdlet 返回一个对象，该对象表示 IPAM 服务器提供的一项可选功能。

## 备注

## 相关链接

[Get-IpamCapability](./Get-IpamCapability.md)

[Enable-Ipam Capability](./Enable-IpamCapability.md)

