---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: microsoft.windows.kits.hardware.certification.management.dll-Help.xml
Module Name: HardwareCertification
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hardwarecertification/merge-hwcerttestcollectionfromxml?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Merge-HwCertTestCollectionFromXml
---

# 从XML文件中合并硬件认证测试集合

## 摘要
将来自多个测试集合文件的测试结果信息合并到一个测试集合中。

## 语法

```
Merge-HwCertTestCollectionFromXml [-LiteralPath] <String[]> [-ValidationXmlPath <String>]
 [-HckBuildVersion <String>] [<CommonParameters>]
```

## 描述
`Merge-HwCertTestCollectionFromXml` cmdlet 将来自多个 `.xml` 文件的测试结果信息合并到一个测试集合中。有关更多详细信息，请参阅微软开发者网络（MSDN）库中的 [Windows Hardware Certification Kit 下载](https://go.microsoft.com/fwlink/?LinkId=614978)。

你可以使用 `Export-HwCertTestCollectionToXml` cmdlet 将合并后的测试集合导出为.xml文件。此外，还可以使用 `New-HwCertTestCollectionExcelReport` cmdlet 生成包含测试结果的Microsoft Excel报告。

## 示例

### 示例 1：合并两个测试集合文件
```
PS C:\> Merge-HwCertTestCollectionFromXml -LiteralPath ("C:\Temp\BasicTest.xml", "C:\Temp\CertificationTest.xml")
```

这个命令将两个测试集合文件中的结果合并到一起。该命令指定了名为BasicTest.xml和CertificationTest.xml的文件。

### 示例 2：合并两个测试集合文件并导出结果信息
```
PS C:\> Merge-HwCertTestCollectionFromXml -LiteralPath ("C:\Temp\BasicTest.xml", "C:\Temp\CertificationTest.xml") | Export-HwCertTestCollectionToXml -Output "C:\Temp\Merged.xml"
```

该命令将两个测试集合文件中的结果合并，并将测试结果信息导出到一个名为 Merged.xml 的 .xml 文件中。该命令合并的文件分别是 BasicTest.xml 和 CertificationTest.xml。随后，通过使用管道运算符（pipeline operator），该命令将合并后的结果传递给 **Export-HwCertTestCollectionToXml** cmdlet，由该 cmdlet 负责导出结果。

### 示例 3：合并多个测试集文件并导出结果信息
```
PS C:\> Get-ChildItem -Recurse "C:\Temp\*.xml" | Merge-HwCertTestCollectionFromXml | Export-HwCertTestCollectionToXml -Output "C:\Temp\Merged.xml"
```

该命令会将所有测试集合文件中的结果合并到指定文件夹中，并将合并后的测试结果信息导出到一个名为 Merged.xml 的 .xml 文件中。该命令使用 **Get-ChildItem** cmdlet 来获取 C:\Temp 文件夹中的所有 .xml 文件。如需更多信息，可输入 `Get-Help Get-ChildItem`。随后，该命令通过管道运算符将这些 .xml 文件传递给 **Merge-HwCertTestCollectionFromXml** cmdlet，由该 cmdlet 负责合并测试结果。最后，该命令将合并后的结果传递给 **Export-HwCertTestCollectionToXml** cmdlet，由该 cmdlet 完成结果的导出操作。

## 参数

### -HckBuildVersion
指定一个 HCK 构建版本。此 cmdlet 仅合并与该构建版本匹配的结果。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Build, Version

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LiteralPath
指定一个文件路径数组。这些文件路径用于测试 collection.xml 文件。

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

### -ValidationXmlPath
指定用于验证的测试集合.xml文件的路径。该cmdlet会将新的测试集合与验证集合作比较，以确保至少存在一个验证结果。验证过程有助于确认从子实验室集合中合并的所有测试都符合原始测试集合的目标要求。

要获取用于验证的测试集合文件，请使用 `New-HwCertTestCollection` cmdlet 以及 `Export-HwCertTestCollectionToXml` cmdlet。

```yaml
Type: String
Parameter Sets: (All)
Aliases: XML

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Windows.Kits.Hardware.Certification.TestCollectionRecord

## 备注

## 相关链接

[将HwCertTestCollection导出为XML格式](./Export-HwCertTestCollectionToXml.md)

[Merge-HwCertTestCollectionFromPackage](./Merge-HwCertTestCollectionFromPackage.md)

[New-HwCertTestCollection](./New-HwCertTestCollection.md)

