---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BackgroundIntelligentTransfer.Management.dll-Help.xml
Module Name: BitsTransfer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitstransfer/resume-bitstransfer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Resume-BitsTransfer
---

# 简历 - BitsTransfer

## 摘要
恢复BITS传输作业。

## 语法

```
Resume-BitsTransfer [-BitsJob] <BitsJob[]> [-Asynchronous] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Resume-BitsTransfer` cmdlet 可以恢复一个或多个被暂停的背景智能传输服务（Background Intelligent Transfer Service，简称 BITS）传输作业。如果 BITS 传输已经在运行中，该 cmdlet 将不会执行任何操作。您可以使用 `Get-BitsTransfer` cmdlet 查看传输作业的当前状态。

默认情况下，`Resume-BitsTransfer` cmdlet 会重新启动传输作业，并使其以同步方式进行；即使原始作业被指定为异步传输作业也是如此。你可以利用这种特性将一个异步传输作业转换为同步传输作业。在以下任一条件成立的情况下，都可以执行这一操作：

- The asynchronous transfer job was created outside cmdlets.

- The asynchronous transfer job was created through the **Start-BitsTransfer** cmdlet.

如果您想将传输作业重新启动为异步传输，请使用 *Asynchronous* 参数。

## 示例

### 示例 1：恢复当前用户拥有的所有 BITS 数据传输作业
```
PS C:\> Get-BitsTransfer | Resume-BitsTransfer
```

此命令会恢复当前用户所拥有的所有BITS传输作业。

当作业完成或进入错误状态后，命令提示符会重新显示。`Get-BitsTransfer` cmdlet 的输出是一组 `BitsJob` 对象，这些输出会被传递给 `Resume-BitsTransfer` cmdlet。如果任何 BITS 传输作业已经在运行中，它们将会继续执行。

### 示例 2：恢复一个最初被暂停的新 BITS（巴西信息科技学院）传输任务
```
PS C:\> $Bits = Start-BitsTransfer -DisplayName "MyJob" -Suspended
PS C:\> Add-BitsTransfer -BitsJob $Bits  -ClientFileName C:\myFile -ServerFileName http://www.mysite.com/file1
PS C:\> Resume-BitsTransfer -BitsJob $Bits -Asynchronous
```

此命令会恢复一个最初被暂停的新BITS传输任务，并立即返回命令提示符。

第一个命令创建了一个处于“暂停状态”的新的**BitsJob**对象，然后将其存储在$Bits变量中。

第二个命令会将一个文件添加到新的 **BitsJob** 对象的传输队列中，该对象存储在 $Bits 变量中。

第三个命令使用了 **BitsJob** 参数，将该参数传递给存储在 `$Bits` 变量中的 **BitsJob** 对象，并将其传给 **Resume-BitsTransfer** cmdlet。这个命令会启动 BITS 数据传输任务。

### 示例 3：根据指定的显示名称恢复 BITS 数据传输
```
PS C:\> Get-BitsTransfer -Name "TestJob01" | Resume-BitsTransfer
```

此命令会恢复由显示名称“TestJob01”标识的BITS传输过程。

任务完成后或任务进入错误状态后，命令提示符会重新显示。`Get-BitsTransfer` cmdlet 的输出是一个 `BitsJob` 对象，该对象会被传递给 ` Resume-BitsTransfer` cmdlet。如果 BITS 传输任务已经处于活动状态，它将继续执行。

## 参数

### -Asynchronous
表示该cmdlet在后台处理BITS传输任务。当BITS传输任务恢复后，命令提示符会立即重新显示。返回的`BitsJob`对象可用于监控状态和进度。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: as

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -BitsJob
用于指定需要恢复的 BITS 传输作业数组。您可以从返回 **BitsJob** 对象的其他 Cmdlet（例如 **Get-BitsTransfer** Cmdlet）中将该参数的值通过管道传递过来。

```yaml
Type: BitsJob[]
Parameter Sets: (All)
Aliases: b

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.BackgroundIntelligentTransfer.Management.BitsJob[]
此cmdlet接受一个或多个**BitsJob**对象作为输入，这些对象会填充*BitsJob*参数的值。

## 输出

### Microsoft.BackgroundIntelligentTransfer.Management.BitsJob[]
当使用“异步（Asynchronous）”参数调用此cmdlet时，它会将与恢复的BITS传输任务相关联的**BitsJob**对象作为输出结果返回。否则，不会生成任何输出。

## 备注
* You can cancel a transfer job that is running in synchronous mode (foreground priority) by pressing CTRL+C.

## 相关链接

[Add-BitsFile](./Add-BitsFile.md)

[完成位传输](./Complete-BitsTransfer.md)

[Get-BitsTransfer](./Get-BitsTransfer.md)

[Remove-BitsTransfer](./Remove-BitsTransfer.md)

[Set-BitsTransfer](./Set-BitsTransfer.md)

[开始比特传输](./Start-BitsTransfer.md)

[暂停比特传输](./Suspend-BitsTransfer.md)

