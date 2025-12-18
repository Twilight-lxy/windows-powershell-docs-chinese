---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/set-sbecactiveconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-SbecActiveConfig
---

# Set-SbecActiveConfig

## 摘要
为正在运行的设置和启动事件收集器（Setup and Boot Event Collector）配置新的活动状态（active configuration）。

## 语法

```
Set-SbecActiveConfig [-Content] <String[]> [[-OldTimestamp] <UInt64>] [-Continue] [[-ComputerName] <String[]>]
 [[-CimSession] <CimSession[]>] [<CommonParameters>]
```

## 描述
`Set-SbecActiveConfig` cmdlet 用于为正在运行的 Setup 和 Boot Event Collector 设置新的活动配置。

新的配置会经过有效性检查，如果通过检查，则会被应用到正在运行的收集器实例及其当前的配置文件中，这样即使在系统重启后，该配置也会被保留并继续使用。之前的配置会被保存在一个备份文件中，这允许你随时撤销所做的任何更改。

你可以使用 `Get-SbecActiveConfig` 和 `Set-SbecActiveConfig` 来原子性地修改配置，具体操作如下：

1. Get the old configuration text and timestamp with **Get-SbecActiveConfig**.
2. Modify the configuration text.
3. Pass the text and timestamp (using the *OldTimestamp* parameter) to **Set-SbecActiveConfig**.

如果指定了 *OldTimestamp* 参数，收集器会检查在这段时间内活动配置是否发生了变化。

如果这次检查成功，新的配置就会被应用；否则，将会返回一个错误信息。

如果之前的配置是从备份文件中恢复的（例如，通过使用 `Undo-SbecActiveConfig` 命令），那么该配置会保留其最初设置时的原始时间戳；而其当前的时间戳则是恢复时的时间。你可以使用 `Get-SbecBackupConfig` 命令来获取原始时间戳。对于这样的配置来说，`Set-SbecActiveConfig` 命令中的 `OldTimestamp` 参数可能会匹配之前配置的当前时间戳或原始时间戳。

在配置被设置之前，其文本会先进行规范化处理：所有回车符（`\r`）都会被删除，同时配置文件末尾的任何空行也会被清除。当配置需要被保存到文件中以供后续使用时，这些回车符会被适当地重新添加回去。

您必须具有内置管理员权限才能运行此cmdlet。

## 示例

### 示例 1：设置活动配置
```
PS C:\> Set-SbecActiveConfig -Content $NewConfig | Format-List
```

这个命令用于设置配置参数，并在遇到错误时抛出异常。`Format-List`用于对返回的信息进行格式化处理。

### 示例 2：从文件中设置激活的配置
```
PS C:\> Get-Content MyConfig.xml | Set-SbecActiveConfig -Continue | Format-List
```

这个命令用于设置配置参数，执行过程中不会抛出错误。“Format-List”命令用于格式化返回的信息。

### 示例 3：将配置设置为一个原子性修改（即一次性的、不可分割的修改操作）
```
PS C:\> do { $prev = Get-SbecActiveConfig; $res = Set-SbecActiveConfig -Content (Modify-MyConfig $prev.Content) -OldTimestamp $prev.Timestamp -Continue } while ($res.ErrorType -eq 5); if ($res.Success) { ... } else { ... }
```

这个命令将新的配置设置为对先前配置的一次原子性修改（即整个修改过程是不可分割的）。

如果原子性（即操作的不可分割性）被破坏了，代码会通过获取新的配置并再次对其进行修改来进行重试。

## 参数

### -CimSession
通过远程会话在远程计算机上运行该 cmdlet。输入一个会话对象（例如 **New-CimSession** 或 **Get-CimSession** cmdlet 的输出结果），或者这些对象的数组。默认情况下，该 cmdlet 会在本地计算机上运行。有关更多信息，请参阅 About_CimSession。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定您希望执行操作的计算机名称。您可以分别为每台计算机指定一个完全 qualified domain name (FQDN)、NetBIOS 名称或 IP 地址。有关更多信息，请参阅 MSDN 上的 [Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Content
指定要设置为活跃状态的配置。此参数的可接受值为：

- A multiline string.
Use `\n` to indicate line breaks.
- An array of one-line strings.
This cmdlet merges the array.
- A mix of multiline strings and string arrays.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Continue
指定如果操作失败时不会抛出异常。相反，调用者应该检查 cmdlet 的输出以获取错误信息。

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
指定上一个有效配置的时间戳。这种方式可以实现配置的原子性更改（即配置状态的改变是不可分割的、不会被部分修改的）。每个配置都有一个时间戳（最后一次设置或恢复该配置时的时间），以及一个原始时间戳（如果该配置是恢复来的，那么原始时间戳就是最初设置该配置的时间；否则，原始时间戳与当前的有效配置的时间戳相同）。此操作会检查 `OldTimestamp` 的值是否与当前有效配置的普通时间戳或原始时间戳相匹配，从而确保自上次查看该配置以来，该配置没有被修改过。如果两个时间戳不匹配，则会返回一个错误。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### `string[]`
配置文本与*Content*参数中的内容相同。

## 输出

### 哈希表
哈希表包含以下元素：

- Success
- NewTimestamp
- ErrorType
- ErrorString
- WarningString
- InfoString

The `<ErrorType>` element contains 0 on success.
If a failure occurs, `<ErrorType>` has a code that describes the error:

- 1 (bad argument format)
- 2 (bad argument value)
- 3 (resource (socket) open error)
- 4 (persistence (backup configuration file) error)
- 5 (atomicity error (that is, the old timestamp does not match)

The Success element is $True on success, $False otherwise.

The `<NewTimeStamp>` element contains the timestamp of the newly restored configuration, that is, the time when it was restored, if this operation is successful, the current original timestamp if the timestamp check fails, or $Null on other failures.

ErrorString, WarningString, and InfoString contain detailed error messages.
`<ErrorString>` contains information only if an error occurs.

## 备注

## 相关链接

[Get-SbecActiveConfig](./Get-SbecActiveConfig.md)

[Restore-SbecBackupConfig](./Restore-SbecBackupConfig.md)

[Test-SbecActiveConfig](./Test-SbecActiveConfig.md)

[Test-SbecConfig](./Test-SbecConfig.md)

[Undo-SbecActiveConfig](./Undo-SbecActiveConfig.md)

