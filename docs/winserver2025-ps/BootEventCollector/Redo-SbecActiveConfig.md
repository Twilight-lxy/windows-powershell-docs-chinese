---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/redo-sbecactiveconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Redo-SbecActiveConfig
---

# 重新执行 SbecActiveConfig 配置操作

## 摘要
重新应用对当前活动配置所做的更改。

## 语法

```
Redo-SbecActiveConfig [[-OldTimestamp] <UInt64>] [-Continue] [[-ComputerName] <String[]>]
 [[-CimSession] <CimSession[]>] [<CommonParameters>]
```

## 描述
`Redo-SbecActiveConfig` cmdlet 用于重新应用对当前活动配置所做的修改。此操作与撤销对配置的修改相反。

如果有多个备份配置文件可用，您可以依次执行“撤销”（Undo）和“重做”（Redo）操作，以便在各种配置之间来回切换。

如果之前处于活动状态的配置没有被恢复，而是被重新设置（或者在恢复后被标记为“检查点”），那么该配置会被保存在一个备份文件中。当连续执行多个“撤销/重做/恢复”命令时，这些过程中的中间状态并不会被保存到新的备份文件中。如果某个配置在一段时间内（例如一小时）保持不变，那么它就会自动被视为一个“检查点”。

你可以使用 *OldTimestamp* 参数来原子地修改配置。

恢复后的配置会再次被检查其有效性；如果配置已经损坏，那么该配置将会被拒绝（即无法被接受）。

您必须具有内置管理员权限才能运行此命令。

## 示例

### 示例 1：重新执行配置更改
```
PS C:\> Redo-SbecActiveConfig -Continue | Format-List
```

这个命令用于重新执行配置更改操作。“Format-List”命令会显示该命令返回的信息。

### 示例 2：重新执行两次配置更改
```
PS C:\> $res = Redo-SbecActiveConfig; $res = Redo-SbecActiveConfig -OldTimestamp $res.OriginalTimestamp
```

这个命令会连续执行两次配置更改操作，确保在此期间不会有其他任何更改被进行，并且在执行过程中会抛出错误。这要求之前的配置更改（从最近的一次开始）至少已经被撤销过两次。

## 参数

### -CimSession
通过远程会话在远程计算机上运行相应的 cmdlet。可以输入一个会话对象（例如 `New-CimSession` 或 `Get-CimSession` cmdlet 的输出结果），或者这些对象的数组。默认情况下，该 cmdlet 会在本地计算机上运行。有关更多信息，请参阅 “About_CimSession”。

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
指定您希望在其上执行操作的计算机的名称。您可以分别为每台计算机指定一个完全合格的域名（FQDN）、NetBIOS名称或IP地址。有关更多信息，请参阅MSDN上的[Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

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
说明：如果操作失败，该操作不会抛出异常。相反，调用者应该检查 cmdlet 的输出以获取错误信息。

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
指定上一个有效配置的时间戳。这提供了一种对配置进行原子级更改（即不可分割的、连续的操作）的方法。每个配置都有一个时间戳（最后一次设置或恢复该配置的时间），以及一个原始时间戳（如果该配置是恢复过来的，则为最初设置的时间；否则与普通时间戳相同）。此操作会检查 *OldTimestamp* 的值是否与当前有效配置的普通时间戳或原始时间戳相匹配，从而确保自您上次查看该配置以来，该配置未被修改。如果这两个值不匹配，则会返回错误信息。

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

### 没有（需要处理的内容）。

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

The Success element is $True on success, $False otherwise.

The `<NewTimeStamp>` element contains the timestamp of the newly restored configuration (that is, the time when it was restored) if this operation is successful, the current original timestamp if the timestamp check fails, or $Null on other failures.

The `<OriginalTimestamp>` element contains the original timestamp of the newly restored configuration on success, the current original timestamp on the timestamp check failure, or $Null on other failures.

`<ErrorString>`, `<WarningString>`, and `<InfoString>` contain detailed error messages.
`<ErrorString>` contains information only if an error occurs.

## 备注

## 相关链接

[Checkpoint-SbecActiveConfig](./Checkpoint-SbecActiveConfig.md)

[Get-SbecBackupConfig](./Get-SbecBackupConfig.md)

[Restore-SbecBackupConfig](./Restore-SbecBackupConfig.md)

[Set-SbecActiveConfig](./Set-SbecActiveConfig.md)

[Undo-SbecActiveConfig](./Undo-SbecActiveConfig.md)

