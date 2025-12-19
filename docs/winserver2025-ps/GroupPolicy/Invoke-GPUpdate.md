---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/invoke-gpupdate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Invoke-GPUpdate
---

# 调用 GPUpdate 命令

## 摘要

在指定的计算机上安排远程组策略更新任务。

## 语法

### NonSyncSet（默认值）

```
Invoke-GPUpdate [-AsJob] [-Boot] [[-Computer] <String>] [[-RandomDelayInMinutes] <Int32>] [-Force]
 [-LogOff] [-Target <String>] [<CommonParameters>]
```

### SyncSet

```
Invoke-GPUpdate [-AsJob] [-Boot] [[-Computer] <String>] [[-RandomDelayInMinutes] <Int32>] [-LogOff]
 [-Target <String>] [-Sync] [<CommonParameters>]
```

## 描述

`Invoke-GPUpdate` cmdlet 通过调度在远程计算机上运行 `Gpupdate` 命令来更新组策略设置（包括那些设置在远程计算机上的安全设置）。你可以将此 cmdlet 与脚本结合使用，以便在一组计算机上定时执行 `Gpupdate` 命令。

刷新操作可以设置为立即开始更新策略设置，也可以等待指定的时间（最长为31天）。为了避免对网络造成负担，刷新时间会随机延迟一段时间后再执行。

## 示例

### 示例 1：在当前计算机上安排一次组策略更新

```powershell
Invoke-GPUpdate
```

此命令会在您运行 `Invoke-GPUpdate` cmdlet 的计算机上安排一次组策略更新任务。

### 示例 2：在远程计算机上安排组策略更新

```powershell
Invoke-GPUpdate -Computer "CONTOSO\COMPUTER-02" -Target "User"
```

此命令会在名为 `CONTOSO\COMPUTER-02` 的远程计算机上安排一次组策略更新，该更新仅以同步模式来更新用户策略设置。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用该参数来执行需要很长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。

要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Boot

表示在应用组策略设置后，该 cmdlet 会重新启动计算机。这对于那些不在后台更新周期中处理组策略、而是在计算机启动时才处理组策略的客户端扩展程序（CSE）来说是必需的；例如，这些扩展程序负责根据每台计算机的软件安装策略进行相应的操作。

如果没有需要重启的名为“CSE”的组件，则此参数无效。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Computer

指定此cmdlet为哪台计算机安排组策略更新。您可以按照以下格式之一来指定计算机名称：

- Full computer name (FQDN computer name); for example, `computer-01.sales.contoso.com`.

- Fully qualified domain name (FQDN)\computer name; for example, `sales.contoso.com\computer-01`.

- NetBIOS domain name\computer name; for example, `sales\computer-01`.

- Computer name (host name): for example, `computer-01`.

如果未指定计算机名称，则运行此cmdlet的计算机的组策略设置将被更新。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DNSHostName

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Force

强制命令运行，而无需请求用户确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: NonSyncSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogOff

表示在更新策略设置后，该cmdlet会使当前用户登出。这对于那些不在后台更新周期中处理组策略（Group Policy），而是在用户登录时才处理组策略的组策略客户端扩展程序（Group Policy Client-Side Extensions, CSEs）来说是必需的。例如，针对用户的软件安装策略设置以及文件夹重定向（Folder Redirection）扩展程序就属于这类情况。

如果没有需要登出的此类CSE（Central Security Elements），则此参数没有任何效果。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RandomDelayInMinutes

指定任务调度器在运行计划好的组策略更新之前会等待的延迟时间（以分钟为单位），同时会添加一个随机因子以降低网络负载。

您可以指定延迟时间，范围从0分钟到最长44640分钟（31天）：

- A value of 0 causes the Group Policy refresh to run as soon as the gpupdate task has been
  scheduled.

- A value in the range of 1 minute to the maximum value of 44640 minutes cause the Group Policy
refresh to delay the specified number of minutes plus a random offset before starting the Group
Policy refresh.

```yaml
Type: Int32
Parameter Sets: (All)
Aliases: RandomnessInMinutes

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Sync

这表示该 cmdlet 会同步处理下一个需要执行的前台组策略应用。前台组策略应用会在计算机启动和用户登录时自动运行。你可以使用 **Target** 参数来指定针对用户、计算机还是两者都进行该操作。

在客户端计算机上，默认情况下，组策略（Group Policy）会在计算机启动时同步执行，在用户登录时异步执行。

在服务器上，默认情况下，组策略（Group Policy）会在计算机启动时以及用户登录时同步执行相关操作。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: SyncSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Target

指定仅更新用户策略设置或计算机策略设置。默认情况下，会同时更新用户策略设置和计算机策略设置。

此参数的可接受值为：

- User
- Computer

如果未指定 **Target** 参数，则会同时更新用户和计算机的策略设置。

```yaml
Type: System.String
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

### 无

这个cmdlet不接受任何对象作为输入。

## 输出

### 无

此cmdlet不会生成任何输出。

## 备注

* This cmdlet does not support scheduling a Group Policy refresh for computers running Windows XP or
  earlier.
* In order to successfully schedule a Group Policy refresh for computers using this cmdlet, the
  following Firewall rules must be set on each client computer to allow the following connections:

- Remote Scheduled Tasks Management (RPC)
- Remote Scheduled Tasks Management (RPC-ERMAP)
- Windows Management Instrumentation (WMI-IN)

## 相关链接

