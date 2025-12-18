---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/get-sbecbackupconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-SbecBackupConfig
---

# Get-SbecBackupConfig

## 摘要
获取可用于恢复的备份配置文件。

## 语法

```
Get-SbecBackupConfig [[-ComputerName] <String[]>] [[-CimSession] <CimSession[]>] [<CommonParameters>]
```

## 描述
`Get-SbecBackupConfig` cmdlet 可以获取可用于恢复的备份配置文件。

每当在“启动事件收集器”中设置新的配置时，旧的配置会会被保存到一个备份文件中（更多详情请参见 Checkpoint-SbecActiveConfig）。通常，这些备份文件的名称中包含 UTC 时间戳，格式为 YYYYMMDDhhmmssfffffff（其中 “f” 表示秒的小数部分），这有助于您追踪配置变更的历史记录并恢复旧配置。如果该收集器是使用 *noCfgHistory* 参数启动的，则只会保存一个最新的配置到固定名称的文件中，并且会使用该文件的最后修改时间戳来标记当前的配置时间。要为该服务指定这个参数，可以在注册表中创建值 “HKLM:\SYSTEM\CurrentControlSet\Services\BootEventCollector\Parameters\noCfgHistory”，并将其类型设置为 REG_DWORD，值为 1。

`Get-SbecBackupConfig` 会返回所有可用的备份配置文件列表，这些文件按照创建时间的先后顺序排列（最新的在列表最前面，最早的在列表最后面）。你可以使用 `Restore-SbecBackupConfig` 显式地恢复这些文件，或者通过 `Undo-SbecActiveConfig` 和 `Redo-SbecActiveConfig` 依次处理它们。

即使可以创建带有未来时间戳的备份文件（无论是手动创建，还是当计算机的时间设置突然回退时），并且这些文件可以通过 `Get-SbecBackupConfig` 命令列出，但它们会被 `Undo-SbecActiveConfig` 和 `Redo-SbecActiveConfig` 命令忽略。你可以使用 `Restore-SbecActiveConfig` 命令来恢复这些备份文件。

此命令返回一个哈希表，其中包含 `<OriginalTimestamp>` 和 `<Files>` 两个元素。`<OriginalTimestamp>` 元素存储了当前活动配置的原始时间戳（即该配置首次被设置的时间）。您可以将这个时间戳与备份文件的时间戳进行比较，以确定哪个配置是处于活动状态，以及哪些配置可以通过 “撤销”（Undo）和 “重做”（Redo）命令来恢复。`<OriginalTimestamp>` 的格式为二进制的 FILETIME 格式，与其他 Sbec 命令中的时间戳格式相同。

你可以使用以下代码将二进制的 FILETIME 格式转换为 PowerShell 中的时间格式：`[DateTime]::FromFileTimeutc($filetime)`

你可以使用以下代码将 PowerShell 中的时间转换为 FILETIME 格式：`$datetime.ToFileTimeUtc()`

你可以使用以下代码将 PowerShell 中的时间（如果标记为 UTC 时间）转换为配置备份文件名中使用的时间戳格式：`$datetime.ToString("yyyyMMddHHmmssfffffff")`

反向转换可以通过以下代码完成：`[DateTime]::ParseExact($fnametm, "yyyyMMddHHmmssfffffff", $null, "AssumeUniversal, AdjustToUniversal")`

要检查某个 PowerShell 时间是否被标记为 UTC 时间，请使用以下代码：`$datetime.Kind -eq "utc"`

你可以使用以下代码将PowerShell中的时间从本地表示形式转换为UTC表示形式：`[DateTime]::FromFileTimeUtc($datetime.ToFileTimeUtc())`

`<Files>` 元素包含一个数组，其中列出了所有可用的备份文件。每个条目都是一个哈希值，其中包含以下字段：  
- `Name`（文件名）；  
- `Timestamp`（原始时间戳，采用 FILETIME 格式）；  
- `Time`（原始时间戳转换为 PowerShell 的 DateTime 格式，并显示为本地时间，以便于使用）。  

数组中的条目按照创建时间的顺序排列，从最新到最旧依次排列。

您必须具有内置管理员权限才能运行此命令。

## 示例

### 示例 1：获取可用的备份配置文件
```
PS C:\> Get-SbecBackupConfig | Format-List
```

这个命令会获取所有可用的备份配置文件列表，并使用管道操作符（pipeline operator）将这些文件传递给 `Format-List` 函数进行处理。

## 参数

### -CimSession
通过远程会话在远程计算机上运行该cmdlet。可以输入一个会话对象（例如`New-CimSession`或`Get-CimSession` cmdlet的输出结果），或者这些对象的数组。默认情况下，该cmdlet会在本地计算机上运行。有关更多信息，请参阅“关于_CimSession”。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
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
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的选项）。

## 输出

### 哈希表
此cmdlet返回一个包含两个元素的哈希表：

- `<OriginalTimestamp>`
- `<Files>`

The `<OriginalTimestamp>` element contains the original timestamp (that is, the time it was originally set) of the current active configuration in FILETIME format.

The `<Files>` element contains an array of entries describing the available backup files.
Each entry is a hash with fields:

- `<Name>`
- `<Timestamp>`
- `<Time>`

`<Name>` contains the file name, `<Timestamp>` contains its original timestamp in the FILETIME format, and `<Time>` contains its original timestamp converted to the PowerShell DateTime format in local time, for convenience.
The entries in the array are ordered from the most recent to the oldest.

## 备注

## 相关链接

[Checkpoint-SbecActiveConfig](./Checkpoint-SbecActiveConfig.md)

[Redo-SbecActiveConfig](./Redo-SbecActiveConfig.md)

[Restore-SbecBackupConfig](./Restore-SbecBackupConfig.md)

[Undo-SbecActiveConfig](./Undo-SbecActiveConfig.md)

