---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/convertfrom-cipolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: ConvertFrom-CIPolicy
---

# 将 CIP 政策转换为其他格式

## 摘要
将包含代码完整性策略的.xml文件转换为二进制格式。

## 语法

```
ConvertFrom-CIPolicy [-XmlFilePath] <String> [-BinaryFilePath] <String> [<CommonParameters>]
```

## 描述
`ConvertFrom-CIPolicy` cmdlet 可将包含代码完整性策略的 `.xml` 文件转换为二进制格式。您可以将该策略的二进制版本安装到计算机上。

## 示例

#### 示例 1：转换保险单
```
PS C:\> ConvertFrom-CIPolicy -XmlFilePath ".\Policy03.xml" -BinaryFilePath "Policy03.bin"
C:\Policies\Policy03.bin
```

此命令会将 Policy03.xml 中的定义转换为名为 Policy03.bin 的二进制文件。控制台会显示该二进制文件的完整路径。

## 参数

### -BinaryFilePath
指定输出转换后的策略二进制文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: bin

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -XmlFilePath
指定该cmdlet要转换的.xml策略文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: xml

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-CIPolicy](./Get-CIPolicy.md)

[Merge-CIPolicy](./Merge-CIPolicy.md)

[New-CIPolicy](./New-CIPolicy.md)

