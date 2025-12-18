---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/checkpoint-sbecactiveconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Checkpoint-SbecActiveConfig
---

# 检查Checkpoint-SbecActiveConfig的状态

## 摘要
创建一个配置检查点。

## 语法

```
Checkpoint-SbecActiveConfig [[-OldTimestamp] <UInt64>] [-Continue] [[-ComputerName] <String[]>]
 [[-CimSession] <CimSession[]>] [<CommonParameters>]
```

## 描述
`Checkpoint-SbecActiveConfig` cmdlet 用于为当前处于活动状态的启动事件收集器（Boot Event Collector）配置创建一个检查点。

检查点允许您日后通过使用 **Undo-SbecActiveConfig**、**Redo-SbecActiveConfig** 和 **Restore-SbecBackupConfig** 这些 cmdlet 来恢复到之前的配置状态。这些检查点记录了那些被确认为正确的配置版本，当新的配置出现问题时，您可以依赖这些检查点来恢复到之前的正确配置。例如，如果您昨天更改了某个配置，但今天发现该配置存在问题，并且希望恢复到更改前的状态，那么就可以使用昨天保存的检查点配置。

大多数检查点都是自动创建的，但在极少数情况下，您可能需要手动创建它们。当当前配置尚未被保存为检查点，并且发生了以下事件之一时，系统会自动创建检查点：

- The Collector service is restarted.
- The configuration that was running for more than an hour is replaced with another configuration.
In this case, the old configuration is checkpointed before being replaced.
- A new configuration is set with **Set-SbecActiveConfig**.
This new configuration is immediately checkpointed.

检查点（checkpoint）的作用是确保当前配置能够被保留下来，但它并不会立即生成备份配置文件。只有当配置发生变化时，才会将已标记为检查点的当前配置保存到备份文件中。

重复进行检查点操作虽然成功了，但实际上并没有产生任何效果，因为这些操作只是标记了系统在未来需要创建备份的配置信息而已。

`Undo-SbecActiveConfig`、`Redo-SbecActiveConfig` 和 `Restore-SbecBackupConfig` 这些 cmdlet 通过浏览备份配置来更改当前配置，但它们不会立即创建检查点。这样你可以查看之前的配置、尝试使用这些配置，并在发现某个配置不适用时随时改变决定，而不会因此产生大量内容相同的冗余检查点和备份文件。当你对某个配置满意后，可以使用 `Checkpoint-SbecActiveConfig` 来创建一个检查点。如果你忘记为某个配置创建检查点，系统会在一小时后自动为其创建一个检查点。

使用 `Get-SbecBackupConfig` 命令来获取备份配置文件的列表。

你可以使用 *OldTimestamp* 参数来原子性地修改配置。

您必须具有内置管理员权限才能运行此cmdlet。

## 示例

#### 示例 1：撤销配置并创建一个检查点
```
PS C:\> Undo-SbecActiveConfig | Format-List; Checkpoint-SbecActiveConfig | Format-List
```

这个命令可以简单地撤销某个配置设置，并创建一个检查点（checkpoint）。**Format-List** 用于格式化该 cmdlet 返回的信息。

### 示例 2：原子性地撤销配置并创建检查点
```
PS C:\> $res = Undo-SbecActiveConfig | Format-List
PS C:\> $res = Checkpoint-SbecActiveConfig -OldTimestamp $res.OriginalTimestamp | Format-LIst
```

这个命令会撤销之前的配置设置，并创建一个检查点（checkpoint），以确保在此期间不会发生其他任何更改；如果过程中出现错误，该命令也会相应地处理这些错误。

## 参数

### -CimSession
通过远程会话在远程计算机上运行该 cmdlet。可以输入一个会话对象（例如 **New-CimSession** 或 **Get-CimSession** cmdlet 的输出结果），或者这些对象的数组。默认情况下，该 cmdlet 会在本地计算机上运行。有关更多信息，请参阅 About_CimSession。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定您希望在其上执行操作的计算机的名称。您可以分别为每台计算机指定一个完全合格的域名（FQDN）、NetBIOS 名称或 IP 地址。有关更多信息，请参阅 MSDN 上的 [Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Continue
这表示如果操作失败，该操作不会抛出异常。相反，调用者应该检查 cmdlet 的输出以获取错误信息。

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

### -OldTimestamp
指定上一个有效配置的时间戳。这提供了一种执行配置原子性更改的方法。

每种配置都有一个时间戳（最后一次设置或恢复该配置的时间），以及一个原始时间戳（如果该配置是恢复的，则为最初设置的时间；否则，原始时间戳与当前配置的时间戳相同）。此操作会检查 `OldTimestamp` 的值是否与当前活动配置的正常时间戳或原始时间戳相匹配，从而确保自上次检查以来活动配置没有发生变化。如果这两个值不匹配，系统将返回一个错误。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 哈希表（Hashtable）
此cmdlet返回一个哈希表，其中包含以下元素：

- `<Success>`
- `<ErrorType>`
- `<ErrorString>`
- `<WarningString>`
- `<InfoString>`

The Success element is $True on success, $False otherwise.
You can use the *Continue* parameter to not throw an error on failure.

The `<ErrorType>` element contains 0 on success.
If a failure occurs, `<ErrorType>` has a code that describes the error:

- 1 - Bad argument format.
- 2 - Bad argument value.
- 3 - Resource (socket) open error.
- 4 - Persistence (backup configuration file) error.
- 5 - Atomicity error (that is, the old timestamp does not match).

`<ErrorString>`, `<WarningString>`, and `<InfoString>` contain detailed error messages.
`<ErrorString>` contains information only if an error occurs.

## 备注

## 相关链接

[Get-SbecBackupConfig](./Get-SbecBackupConfig.md)

[Redo-SbecActiveConfig](./Redo-SbecActiveConfig.md)

[Restore-SbecBackupConfig](./Restore-SbecBackupConfig.md)

[Set-SbecActiveConfig](./Set-SbecActiveConfig.md)

[Undo-SbecActiveConfig](./Undo-SbecActiveConfig.md)

