---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/get-sbecactiveconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-SbecActiveConfig
---

# Get-SbecActiveConfig

## 摘要
从正在运行的设置和启动事件收集器中获取当前活动的配置信息。

## 语法

```
Get-SbecActiveConfig [[-ComputerName] <String[]>] [[-CimSession] <CimSession[]>] [<CommonParameters>]
```

## 描述
`Get-SbecActiveConfig` cmdlet 返回一个包含两个元素的哈希表：`<Content>` 和 `<Timestamp>`。`<Content>` 元素以字符串的形式存储了当前生效的配置内容；`<Timestamp>` 元素则保存了该配置被设置的时间戳，该时间戳是一个 64 位的 FILETIME 值。

你可以使用时间戳来验证配置自上次读取以来是否发生了变化。你还可以利用时间戳获取配置信息，在本地对其进行修改，然后再将其设置回原来的状态，从而确保在这段时间内没有人对配置进行过任何更改。

你可以修改配置文件中的文本内容，使其恢复到上次设置时的精确形式。为此，你需要删除所有的回车符（`\r`），并移除配置文件末尾的任何空行。

当执行此命令失败时，会抛出一个错误。

此命令仅适用于具有内置管理员（Built-in Administrator，简称BA）权限的用户。

## 示例

#### 示例 1：获取当前活动的配置
```
PS C:\> $res = Get-SbecActiveConfig
```

这条命令获取当前的配置信息，并将其存储在 `$res` 变量中。

### 示例 2：转换时间戳
```
PS C:\> $time = [DateTime]::FromFileTimeUtc($res.Timestamp)
```

该命令将返回的时间戳转换为PowerShell格式，然后将其存储在 `$res` 变量中。

### 示例 3：获取配置文件的文本内容
```
PS C:\> $text = $res.Content
```

该命令将配置返回的文本提取为一个字符串，然后将其存储在 `$text` 变量中。

### 示例 4：打印返回的全部信息
```
PS C:\> Get-SbecActiveConfig | Format-List
```

这个命令获取当前的配置信息，并将其传递给 `Format-List` 命令，后者会对结果进行格式化处理。

## 参数

### -CimSession
通过远程会话在远程计算机上运行该cmdlet。可以输入一个会话对象（例如**New-CimSession**或**Get-CimSession** cmdlet的输出结果），或者这些对象的数组。默认情况下，该cmdlet会在本地计算机上运行。有关更多信息，请参阅“About_CimSession”。

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
指定您想要执行操作的计算机名称。对于每台计算机，您可以指定一个完全 Qualified Domain Name（FQDN）、一个 NetBIOS 名称或一个 IP 地址。有关更多信息，请参阅 TechNet 上的 [Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### 哈希表
这个cmdlet返回一个包含两个元素的哈希表：

- `<Content>`
- `<Timestamp>`

The `<Content>` element contains the text of the active configuration as a single string.
The `<Timestamp>` element contains the timestamp when that configuration was set, as a FILETIME 64-bit value.
The common way to see the full result is to pipe it through the **Format-List** cmdlet (alias fl).

## 备注

## 相关链接

[Set-SbecActiveConfig](./Set-SbecActiveConfig.md)

[Test-SbecActiveConfig](./Test-SbecActiveConfig.md)

[测试-SbecConfig](./Test-SbecConfig.md)

