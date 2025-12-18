---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/test-sbecconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-SbecConfig
---

# Test-SbecConfig

## 摘要
验证配置的有效性。

## 语法

```
Test-SbecConfig [-Content] <String[]> [-Continue] [[-ComputerName] <String[]>] [[-CimSession] <CimSession[]>]
 [<CommonParameters>]
```

## 描述
`Test-SbecConfig` cmdlet 用于验证与设置和启动事件收集器（Setup and Boot Event Collector）相关的配置是否正确。

这个cmdlet用于检查配置的有效性，而不会实际应用该配置。它的功能类似于运行`bevtcol.exe -checkOnly`命令，只不过`Test-SbecConfig`会利用正在运行的服务来进行验证。

**Test-SbecConfig** 返回的值是 **Set-SbecActiveConfig** 返回值的一个子集，因为 **Test-SbecConfig** 并不会实际应用该配置。

您必须具有内置管理员权限才能运行此命令。

这个cmdlet也可以使用别名**Validate-SbecConfig**来调用。

## 示例

#### 示例 1：验证配置
```
PS C:\> $res = Test-SbecConfig -Content $NewConfig -Continue
```

这个命令会验证 `$NewConfig` 中的配置内容，然后将结果存储在 `$res` 变量中。由于指定了 “*Continue*” 参数，因此即使出现错误，该命令也不会抛出异常。

### 示例 2：使用流水线验证配置
```
PS C:\> Get-Content MyConfig.xml | Test-SbecConfig -Continue | Format-List
```

这个命令用于验证文件中的配置信息。Format-List 会打印出所有返回的信息，而不会对信息进行任何压缩或处理。

### 示例 3：验证配置并在发现错误时抛出异常
```
PS C:\> $res = Test-SbecConfig -Content (Get-Content MyConfig.xml)
```

从文件中验证配置内容，如果发现错误则抛出异常。

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
指定您想要在其上执行操作的计算机的名称。您可以分别为每台计算机指定一个完全合格的域名（FQDN）、NetBIOS 名称或 IP 地址。有关更多信息，请参阅 MSDN 上的 [Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

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
指定需要验证的配置。该参数的可接受值包括：

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
表示如果操作失败，该操作不会抛出异常。相反，调用者应该查看cmdlet的输出以获取错误信息。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### string[]
配置文本与*Content*参数中的内容相同。

## 输出

### 哈希表
哈希表包含以下元素：

- `<Success>`
- `<ErrorType>`
- `<ErrorString>`
- `<WarningString>`
- `<InfoString>`

The `<ErrorType>` element contains 0 on success.
If a failure occurs, `<ErrorType>` has a code that describes the error:

- 1 (bad argument format)
- 2 (bad argument value)

The `<Success>` element is $True on success, $False otherwise.

`<ErrorString>`, `<WarningString>`, and `<InfoString>` contain detailed error messages.
`<ErrorString>` contains information only if an error occurs.

## 备注

## 相关链接

[Get-SbecActiveConfig](./Get-SbecActiveConfig.md)

[Set-SbecActiveConfig](./Set-SbecActiveConfig.md)

[Test-SbecActiveConfig](./Test-SbecActiveConfig.md)

