---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/restore-sbecbackupconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Restore-SbecBackupConfig
---

# 恢复 SbecBackupConfig 配置

## 摘要
从备份文件中恢复配置。

## 语法

### 名称
```
Restore-SbecBackupConfig -Name <String> [-OldTimestamp <UInt64>] [-Continue] [-ComputerName <String[]>]
 [-CimSession <CimSession[]>] [<CommonParameters>]
```

### 在……时间（或地点）
```
Restore-SbecBackupConfig -At <Object> [-OldTimestamp <UInt64>] [-Continue] [-ComputerName <String[]>]
 [-CimSession <CimSession[]>] [<CommonParameters>]
```

### 在……时间（或地点）Timestamp
```
Restore-SbecBackupConfig -AtTimestamp <UInt64> [-OldTimestamp <UInt64>] [-Continue] [-ComputerName <String[]>]
 [-CimSession <CimSession[]>] [<CommonParameters>]
```

## 描述
`Restore-SbecBackupConfig` cmdlet 从备份文件中恢复启动事件收集器（Boot Event Collector）的配置信息。

如果之前的活动配置没有被恢复，而是被重新设置（或者在恢复后被标记为检查点），那么该配置会被保存在一个备份文件中。当连续执行多次“撤销”/“重做”/“恢复”命令时，这些中间状态下的配置不会被保存到新的备份文件中。如果某个配置在一段时间内保持不变（即没有被修改），那么它就会自动被视为一个检查点。

你可以使用 `OldTimestamp` 参数来原子性地修改配置。

恢复后的配置会再次被检查其有效性；如果配置已经损坏，则会被拒绝接受。

您必须具有内置管理员权限才能运行此cmdlet。

## 示例

#### 示例 1：通过名称恢复备份配置
```
PS C:\> Restore-SbecBackupConfig -Name "Active.xml.201502202002352592047.xml" | Format-List
```

这个命令会恢复名为 Active.xml.201502202002352592047.xml 的备份文件，并使用管道运算符（pipeline operator）将其传递给 Format-List 命令。Format-List 命令会对该操作返回的哈希表进行格式化处理。

#### 示例 2：恢复最近的备份配置
```
PS C:\> $res = Restore-SbecBackupConfig -Name ((Get-SbecBackupConfig).Files[0].Name)
```

此命令会从可用的备份文件列表中恢复最新的备份文件，并通过文件名来识别该文件。

### 示例 3：根据备份的时间来恢复备份文件
```
PS C:\> $res = Restore-SbecBackupConfig -At ((Get-SbecBackupConfig).Files[0].Time)
```

这个命令会从可用的备份文件列表中恢复最新的备份文件，并根据其创建时间来识别该文件。

### 示例 4：根据文件的 FILETIME 时间戳恢复备份
```
PS C:\> $Res = Restore-SbecBackupConfig -AtTimestamp ((Get-SbecBackupConfig).Files[0].Timestamp)
```

该命令会从可用的备份文件列表中恢复最新的备份文件，并通过 FILETIME 时间戳来识别该文件。

### 示例 5：从指定时间点恢复配置
```
PS C:\> $res = Restore-SbecBackupConfig -At 20150219
```

此命令会恢复在2015年2月19日午夜（UTC时间）处于活动状态的备份配置。

## 参数

### -At
指定要恢复的配置文件的时间戳。该参数的可接受值为：

- A **DateTime** object.
- A string.
- A number.
Use the format YYYYMMDDhhmmssfffffff, where f represents the fractions of a second.
---- Values for YYYYMMDD are required.
---- If you don't specify a value for hours, minutes, or seconds, this cmdlet appends zeros for those values.
For example, this cmdlet interprets 201502012033 as February 1st 2015 20:33:00.

有关时间戳格式以及如何转换它们的更多信息，请参阅 Get-SbecBackupConfig。

```yaml
Type: Object
Parameter Sets: At
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AtTimestamp
指定要恢复的配置文件的 FILETIME 时间戳。

有关时间戳格式以及如何转换它们的更多信息，请参阅 Get-SbecBackupConfig。

```yaml
Type: UInt64
Parameter Sets: AtTimestamp
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
通过远程会话在远程计算机上运行相应的 cmdlet。可以输入一个会话对象（例如 **New-CimSession** 或 **Get-CimSession** cmdlet 的输出结果），或者这些对象的数组。默认情况下，该 cmdlet 会在本地计算机上运行。有关更多信息，请参阅 “About_CimSession”。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定您希望在其上执行操作的计算机的名称。您可以分别为每台计算机指定一个完全限定域名（FQDN）、NetBIOS名称或IP地址。有关更多信息，请参阅MSDN上的[Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Continue
该说明指出：如果操作失败，该方法不会抛出异常。相反，调用者应该查看cmdlet的输出以获取错误信息。

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

### -Name
指定要恢复的配置文件的名称。若要获取备份配置文件的列表，请使用 Get-SbecBackupConfig cmdlet。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OldTimestamp
指定上一个活跃配置的时间戳。这样可以实现对配置的原子级更改（即配置状态不会被部分修改）。每个配置都有一个时间戳（最后一次设置或恢复时的时间），以及一个原始时间戳（如果配置是从备份中恢复的，则为最初设置时的时间；否则与当前的时间戳相同）。此操作会检查 `OldTimestamp` 的值是否与当前活跃配置的正常时间戳或原始时间戳相匹配，从而确保自上次查看该配置以来，其状态没有被修改过。如果两个时间戳不匹配，则会返回错误信息。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### HashTable
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

The `<NewTimeStamp>` element contains the timestamp of the newly restored configuration, i.e.
the time when it was restored, if this operation is successful, the current original timestamp if the timestamp check fails, or $Null on other failures.

The `<OriginalTimestamp>` element contains the original timestamp of the newly restored configuration on success, the current original timestamp on the timestamp check failure, or $Null on other failures.

`<ErrorString>`, `<WarningString>`, and `<InfoString>` contain detailed error messages.
`<ErrorString>` contains information only if an error occurs.

## 备注

## 相关链接

[Checkpoint-SbecActiveConfig](./Checkpoint-SbecActiveConfig.md)

[Get-SbecBackupConfig](./Get-SbecBackupConfig.md)

[Redo-SbecActiveConfig](./Redo-SbecActiveConfig.md)

[Set-SbecActiveConfig](./Set-SbecActiveConfig.md)

[Undo-SbecActiveConfig](./Undo-SbecActiveConfig.md)

