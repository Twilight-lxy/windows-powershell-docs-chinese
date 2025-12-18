---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/test-sbecactiveconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-SbecActiveConfig
---

# 测试 SbecActiveConfig 配置

## 摘要
测试当前的“启动事件收集器”（Boot Event Collector）配置是否正常工作。

## 语法

```
Test-SbecActiveConfig [-Content] <String[]> [[-ComputerName] <String[]>] [[-CimSession] <CimSession[]>]
 [<CommonParameters>]
```

## 描述
`Test-SbecActiveConfig` cmdlet 用于检测指定的启动事件收集器（Boot Event Collector）配置是否与当前的活动配置相匹配。

比较是基于配置文件的“标准化”文本进行的，具体方法包括删除所有的回车符（`\r`）以及配置文件末尾的任何空行。文本中的中间空行不会被删除，并且空白字符（如空格、制表符等）在比较过程中是会被考虑在内的。

如果配置相匹配，此命令将返回 `$True`；否则，它将返回 `$False`。

这个命令在执行失败时会抛出错误。

您必须具有内置管理员权限才能运行此命令。

## 示例

### 示例 1：通过管道测试配置文件
```
PS C:\> Get-Content -Path "c:\MyConfig.xml" | Test-SbecActiveConfig
```

这个命令通过将当前配置传递给一个处理流程（pipeline），将其与文件“MyConfig.xml”中的内容进行比较。

### 示例 2：通过参数测试配置文件
```
PS C:\> Test-SbecActiveConfig -Content "(Get-Content -Path "c:\MyConfig.xml")"
```

该命令通过将文件 MyConfig.xml 作为参数传递，来比较当前配置与该文件的内容。

## 参数

### -CimSession
通过远程会话在远程计算机上运行该cmdlet。可以输入一个会话对象（例如**New-CimSession**或**Get-CimSession** cmdlet的输出结果），或者这些对象的数组。默认情况下，该cmdlet会在本地计算机上运行。有关更多信息，请参阅“关于_CimSession”。

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
指定您希望执行操作的计算机名称。您可以分别为每台计算机指定一个完全限定域名（FQDN）、NetBIOS 名称或 IP 地址。有关更多信息，请参阅 MSDN 上的 [Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

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

### -Content
指定要测试的配置。该参数的可接受值为：

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串
配置文本与*Content*参数中的内容相同。

## 输出

### 布尔值（Boolean）
比较的结果：$True 或 $False。

## 备注

## 相关链接

[Get-SbecActiveConfig](./Get-SbecActiveConfig.md)

[Set-SbecActiveConfig](./Set-SbecActiveConfig.md)

[测试-SbecConfig配置](./Test-SbecConfig.md)

