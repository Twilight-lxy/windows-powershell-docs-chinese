---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ps_mmagent_v1.0.cdxml-help.xml
Module Name: MMAgent
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/mmagent/enable-mmagent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-MMAgent
---

# 启用 MMAgent

## 摘要
启用应用程序启动前的预加载功能、操作记录器API功能、页面合并功能以及应用程序的预先启动功能。

## 语法

```
Enable-MMAgent [-ApplicationLaunchPrefetching] [-OperationAPI] [-PageCombining] [-ApplicationPreLaunch]
 [-MemoryCompression] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Enable-MMAgent` cmdlet 可以启用以下一个或多个功能：  
- 应用程序启动前的预加载  
- 操作记录器（Operation Recorder）API 功能  
- 页面合并（Page Combining）  
- 应用程序启动前的预处理（Application Prelaunching）

请指定 *ApplicationLaunchPrefetching* 参数，以帮助提升应用程序的启动性能。应用程序启动预加载功能会促使内存管理代理监控应用程序所访问的数据和代码。随后，内存管理代理会利用这些信息将这些数据和代码预先加载到物理内存中，以便在后续启动时能够更快地使用它们。

请指定 *ApplicationPreLaunch* 参数，以帮助提升应用程序的启动性能。应用程序预启动功能可以预先加载用户近期可能使用到的应用程序，从而减少应用程序切换所需的时间。

请指定 *OperationAPI* 参数，以帮助加速那些需要反复访问相同文件数据的操作。启用此功能后，Windows 的预加载机制将以公开接口的形式被暴露出来。

请指定*PageCombining*参数，以帮助减少操作系统使用的物理内存。页面合并（Page Combining）功能会使内存管理器定期将物理内存中内容相同的页面合并在一起。

## 示例

### 示例 1：启用应用程序启动时的预取功能
```
PS C:\> Enable-MMAgent -ApplicationLaunchPrefetching
```

此命令允许在本地计算机上启用应用程序启动时的预加载功能。

## 参数

### -ApplicationLaunchPrefetching
表示该cmdlet启用了应用程序启动前的预加载功能。

如果您不指定此参数，应用程序启动时的预加载功能将保持当前状态（无论是已启用还是已禁用）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: alp

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ApplicationPreLaunch
表示该 cmdlet 可以实现应用程序的预启动功能。

如果您不指定此参数，应用程序在预启动时的状态将保持不变，无论是启用还是禁用。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: apl

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -MemoryCompression
表示此 cmdlet 使用了内存压缩技术。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: mc

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OperationAPI
表示该 cmdlet 启用了操作记录器（Operation Recorder）API 的功能。

如果您不指定此参数，操作记录器（Operation Recorder）的API功能将保持当前状态，即要么处于启用状态，要么处于禁用状态。

有关操作记录器（Operation Recorder）API的更多信息，请参阅MSDN上的[操作记录器](https://msdn.microsoft.com/library/windows/desktop/hh437575.aspx)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: oa

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PageCombining
表示该cmdlet支持页面合并功能。

如果您不指定此参数，页面合并功能将保持当前状态（即启用或禁用）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: pc

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时建立的最大并发操作数量，以便运行该cmdlet。如果省略此参数或输入`0`值，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值（即并发操作的上限）。此限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

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

[Debug-MMAppPrelaunch](./Debug-MMAppPrelaunch.md)

[Get-MMAgent](./Get-MMAgent.md)

[Set-MMAgent](./Set-MMAgent.md)

[ Disable-MMAgent](./Disable-MMAgent.md)

