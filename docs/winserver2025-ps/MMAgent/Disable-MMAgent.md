---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ps_mmagent_v1.0.cdxml-help.xml
Module Name: MMAgent
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/mmagent/disable-mmagent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-MMAgent
---

# 关闭 MMAgent

## 摘要
禁用应用程序启动时的预加载功能、操作记录器API功能、页面合并功能以及应用程序的预启动过程。

## 语法

```
Disable-MMAgent [-ApplicationLaunchPrefetching] [-ApplicationPreLaunch] [-OperationAPI] [-PageCombining]
 [-MemoryCompression] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Disable-MMAgent` cmdlet 可以禁用以下一个或多个功能：  
- 应用程序启动前的预加载  
- 操作记录器（Operation Recorder）API 功能  
- 页面合并（Page Combining）  
- 应用程序启动前的预览（Application Prelaunching）

有关这些功能的更多详细信息，请参阅 Enable-MMAgent。

## 示例

#### 示例 1：禁用应用程序启动时的预加载功能
```
PS C:\> Disable-MMAgent -ApplicationLaunchPrefetching
```

此命令会禁用本地计算机上应用程序启动时的预加载功能。

## 参数

### -ApplicationLaunchPrefetching
表示该 cmdlet 禁用了应用程序启动时的预加载功能。

如果您不指定这个参数，应用程序启动时的预加载功能将保持当前的状态，无论是启用还是禁用。

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
表示该 cmdlet 禁用了应用程序的预启动功能。

如果您不指定此参数，应用程序的预启动状态将保持不变，即要么处于启用状态，要么处于禁用状态。

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
将cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
表示此cmdlet使用了内存压缩技术。

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
表示该cmdlet禁用了操作记录器（Operation Recorder）API的功能。

如果您不指定此参数，操作记录器（Operation Recorder）API的功能将保持当前状态，即启用或禁用状态不变。

有关操作记录器（Operation Recorder）API的更多信息，请参阅MSDN上的[操作记录器](https://msdn.microsoft.com/library/windowsdesktop/hh437575.aspx)。

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
表示该cmdlet禁用了页面合并功能。

如果您不指定此参数，页面合并功能将保持当前状态，无论是启用还是禁用。

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
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。该限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[调试-MMApp预启动过程](./Debug-MMAppPrelaunch.md)

[Enable-MMAgent](./Enable-MMAgent.md)

[Get-MMAgent](./Get-MMAgent.md)

[Set-MMAgent](./Set-MMAgent.md)

