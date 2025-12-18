---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BranchCacheOrchestrator.cdxml-help.xml
Module Name: BranchCache
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/branchcache/set-bcminsmblatency?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-BCMinSMBLatency
---

# 设置 BCMinSMBLatency

## 摘要
设置客户端和服务器之间必须存在的最小延迟时间，才能使用透明缓存功能。

## 语法

```
Set-BCMinSMBLatency [-LatencyMilliseconds] <UInt32> [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Set-BCMinSMBLatency** 这个 cmdlet 用于设置客户端和服务器之间在启用透明缓存功能之前必须存在的最小延迟。通过使用这个 cmdlet，可以指定分支办公室中的客户端计算机在什么情况下开始根据网络延迟来从内容服务器缓存数据（即在通过广域网 (WAN) 链路下载数据时出现的延迟）。当为该 cmdlet 指定了一个值（即允许开始缓存前的最大往返网络延迟）后，客户端会在网络延迟达到指定值之前不进行数据缓存；如果网络延迟超过该值，则客户端会在从内容服务器接收到数据后立即开始缓存。

例如，如果将往返网络延迟值设置为零（0），那么客户端计算机总会缓存从内容服务器接收到的内容，无论它们请求文件与从内容服务器接收到文件之间的网络延迟高低如何。另一个例子是，如果将往返网络延迟值设置为100毫秒，那么在100毫秒过去之前，客户端不会缓存收到的内容；但在100毫秒之后，客户端就会开始缓存接收到的内容。

默认情况下，该设置的值为 80 毫秒。为了确保客户端计算机始终缓存内容，请将网络延迟值设置为 0。

为了防止缓存被使用（除非网络延迟非常长），请将网络延迟值设置为一个很高的数值。然而，如果使用了过高的延迟值，那么实际上可能并不会出现这么长的延迟情况；在这种情况下，BranchCache功能在你的网络中就会被禁用。

无论此设置是否被禁用或未进行配置，如果广域网（WAN）链路的往返网络延迟超过80毫秒，客户端计算机都会缓存网络文件。

## 示例

#### 示例 1：设置最小延迟
```
PS C:\> Set-BCMinSMBLatency -LatencyMilliseconds 20
```

该命令将客户端与服务器之间在启用透明缓存功能之前必须存在的最小延迟时间设置为20毫秒。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
强制命令运行，而无需询问用户是否确认。

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

### -LatencyMilliseconds
指定客户端和服务器之间必须存在的最小延迟时间，之后BranchCache才会开始缓存内容。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果该cmdlet运行时会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Disable-BC](./Disable-BC.md)

[Reset-BC](./Reset-BC.md)

