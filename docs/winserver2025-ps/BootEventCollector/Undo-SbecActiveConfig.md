---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/undo-sbecactiveconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Undo-SbecActiveConfig
---

# 撤销 SbecActiveConfig 的激活配置

## 摘要
将更改恢复到当前活动的配置状态。

## 语法

```
Undo-SbecActiveConfig [[-OldTimestamp] <UInt64>] [-Continue] [[-ComputerName] <String[]>]
 [[-CimSession] <CimSession[]>] [<CommonParameters>]
```

## 描述
` Undo-SbecActiveConfig` cmdlet 可以将设置和启动事件收集器（Setup and Boot Event Collector）的活跃配置恢复到之前的状态。

如果有多个备份配置文件可用，您可以依次执行“撤销”（Undo）和“重做”（Redo）操作，从而在各个配置之间来回切换。

如果之前激活的配置没有被恢复，而是被重新设置（或者在恢复后被创建为检查点），那么该配置会保存在备份文件中。当连续执行多个“撤销”/“重做”/“恢复”命令时，这些操作过程中的中间状态并不会被保存到新的备份文件中。如果某个配置在一段时间内保持不变（即没有被修改），那么它就会自动被视为一个检查点。

你可以使用 *OldTimestamp* 参数来原子性地修改配置。

恢复后的配置会再次被检查其有效性；如果配置已经损坏，那么该配置将会被拒绝（即无法被使用）。

你必须拥有内置管理员（Built-in Administrator）权限才能运行此命令。

## 示例

### 示例 1：撤销配置更改
```
PS C:\> Undo-SbecActiveConfig -Continue | Format-List
```

此命令会将配置更改恢复到之前的有效配置状态，并将生成的哈希表传递给 `Format-List` 函数进行格式化处理。

### 示例 2：撤销配置更改并处理出现的错误
```
PS C:\> $res = Undo-SbecActiveConfig; $res = Undo-SbecActiveConfig -OldTimestamp $res.OriginalTimestamp
```

这个命令会撤销之前的两个配置更改，确保在此期间没有其他更改被执行到，并且会抛出错误信息。

## 参数

### -CimSession
通过远程会话在远程计算机上运行该cmdlet。可以输入一个会话对象（例如**New-CimSession**或**Get-CimSession** cmdlet的输出结果），或者这些对象的数组。默认情况下，该cmdlet会在本地计算机上运行。有关更多信息，请参阅“About_CimSession”。

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
指定您想要在其上执行操作的计算机的名称。您可以分别为每台计算机指定一个完全 Qualified Domain Name（FQDN）、NetBIOS 名称或 IP 地址。有关更多信息，请参阅 MSDN 上的 [Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

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
指定如果操作失败时不会抛出异常。相反，调用者应该检查cmdlet的输出以获取错误信息。

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
用于指定上一个有效配置的时间戳。这种方式可以实现配置的原子性更改（即配置状态的变更是不可分割的、不会被部分地修改）。每个配置都有一个时间戳（表示该配置最后一次被设置或恢复的时间），以及一个“原始时间戳”（如果该配置是被恢复过来的，那么这个时间戳就是它最初被设置的时间；否则，这个时间戳与当前的有效配置的时间戳相同）。此操作会检查 `OldTimestamp` 的值是否与当前有效配置的普通时间戳或原始时间戳相匹配，从而确保自您上次查看该配置以来，其状态没有发生任何变化。如果这两个时间戳不匹配，则会返回一个错误信息。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的选项）。

## 输出

### 哈希表
哈希表包含以下元素：

- `<Success>`
- `<NewTimestamp>`
- `<OriginalTimestamp>`
- `<ErrorType>`
- `<ErrorString>`
- `<WarningString>`
- `<InfoString>`

The `<ErrorType>` element contains 0 on success.
If a failure occurs, `<ErrorType>` has a code that describes the error:

- 1 (bad argument format)
- 2 (bad argument value)
- 3 (resource (socket) open error)
- 4 (persistence (backup configuration file) error)
- 5 (atomicity error (that is, the old timestamp does not match)

The `<Success>` element is $True on success, $False otherwise.

The `<NewTimeStamp>` element contains the timestamp of the new configuration if this operation is successful, or the current original timestamp if the timestamp check fails, or $Null on other failures.

The `<OriginalTimestamp>` element contains the original timestamp of the newly restored configuration on success, the current original timestamp on the timestamp check failure, or $Null on other failures.

`<ErrorString>`, `<WarningString>`, and `<InfoString>` contain detailed error messages.
`<ErrorString>` contains information only if an error occurs.

## 备注

## 相关链接

[Checkpoint-SbecActiveConfig](./Checkpoint-SbecActiveConfig.md)

[Get-SbecBackupConfig](./Get-SbecBackupConfig.md)

[Redo-SbecActiveConfig](./Redo-SbecActiveConfig.md)

[ Restore-SbecBackupConfig](./Restore-SbecBackupConfig.md)

[Set-SbecActiveConfig](./Set-SbecActiveConfig.md)

