---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ps_mmagent_v1.0.cdxml-help.xml
Module Name: MMAgent
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/mmagent/get-mmagent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MMAgent
---

# Get-MMAgent

## 摘要
用于获取应用程序启动时的预加载状态、操作API的预加载功能、页面合并过程以及应用程序启动前的相关情况。

## 语法

```
Get-MMAgent [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-MMAgent` cmdlet 用于报告以下功能是否已启用：  
- 应用程序启动前的预加载  
- 操作 API 的预加载功能  
- 页面合并  
- 应用程序在启动前的准备（prelaunching）

此cmdlet还可以获取操作记录器API所记录的各种场景中预取文件的最大数量。

## 示例

#### 示例 1：获取预加载功能的状态
```
PS C:\> Get-MMAgent
```

这个命令用于获取应用程序启动时的预加载状态、应用程序预启动功能、操作记录器API的预加载功能以及页面组合的相关信息。同时，该命令还能确定操作记录器API在记录数据时最多可以预加载多少个文件。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `-*Job` 系列的 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值为本地计算机上的当前会话。

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

### -ThrottleLimit
指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### Microsoft.ManagementInfrastructure.CimInstance#MMAgentComponents

## 备注

## 相关链接

[Debug-MMAppPrelaunch](./Debug-MMAppPrelaunch.md)

[Set-MMAgent](./Set-MMAgent.md)

[Enable-MMAgent](./Enable-MMAgent.md)

[ Disable-MMAgent](./Disable-MMAgent.md)

