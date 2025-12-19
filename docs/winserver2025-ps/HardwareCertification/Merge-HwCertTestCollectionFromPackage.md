---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: microsoft.windows.kits.hardware.certification.management.dll-Help.xml
Module Name: HardwareCertification
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hardwarecertification/merge-hwcerttestcollectionfrompackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Merge-HwCertTestCollectionFromPackage
---

# 从包中合并硬件认证测试集合

## 摘要
将来自多个.hckx包文件的测试结果信息合并到一个测试集合中。

## 语法

```
Merge-HwCertTestCollectionFromPackage [-LiteralPath] <String[]> [-Force] [-IncludeAll]
 [-ValidationXmlPath <String>] [-HckBuildVersion <String>] [<CommonParameters>]
```

## 描述
`Merge-HwCertTestCollectionFromPackage` cmdlet 将来自多个 `.hckx` 包文件的测试结果信息合并到一个测试集合中。有关更多详细信息，请参阅微软开发者网络（MSDN）库中的 [Windows 硬件认证工具包下载](https://go.microsoft.com/fwlink/?LinkId=614978)。

你可以使用 `Export-HwCertTestCollectionToXml` cmdlet 将合并后的测试集合导出为 `.xml` 文件。此外，你还可以使用 `New-HwCertTestCollectionExcelReport` cmdlet 生成一份包含测试结果的 Microsoft Excel 报告。

该cmdlet会解析每个.hckx包文件，然后在与被解析文件相同的目录下生成一个缓存的.xml文件。因此，您必须具有对包含.hckx包文件的文件夹的写入权限。

## 示例

### 示例 1：合并两个包文件
```
PS C:\> Merge-HwCertTestCollectionFromPackage -LiteralPath ("C:\Temp\BasicTest.hckx", "C:\Temp\CertificationTest.hckx")
```

这个命令将两个结果合并到两个名为“.hckx”的包文件中。该命令指定了名为“BasicTest.hckx”和“CertificationTest.hckx”的文件。

### 示例 2：合并两个包文件并导出结果信息
```
PS C:\> Merge-HwCertTestCollectionFromPackage -LiteralPath ("C:\Temp\BasicTest.hckx", "C:\Temp\CertificationTest.hckx") | Export-HwCertTestCollectionToXml -Output "C:\Temp\Merged.xml"
```

该命令将两个 `.hckx` 包文件中的内容合并，并将合并后的结果信息导出到一个名为 `Merged.xml` 的 `.xml` 文件中。该命令合并的文件分别是 `BasicTest.hckx` 和 `CertificationTest.hckx`。通过使用管道运算符（pipeline operator），该命令将合并后的结果传递给 `Export-HwCertTestCollectionToXml` cmdlet，由该 cmdlet 负责输出最终的导出结果。

### 示例 3：合并多个包文件并导出结果信息
```
PS C:\> Get-ChildItem -Recurse "C:\Temp\*.hckx" | Merge-HwCertTestCollectionFromPackage | Export-HwCertTestCollectionToXml -Output "C:\Temp\Merged.xml"
```

该命令会将指定文件夹中所有`.hckx`包文件中的测试结果合并，并将合并后的结果信息导出到一个名为`Merged.xml`的`.xml`文件中。该命令使用`Get-ChildItem` cmdlet来获取`C:\Temp`文件夹中的所有`.hckx`文件（如需更多信息，请输入`Get-Help Get-ChildItem`）。接着，该命令通过管道运算符将这些`.hckx`文件传递给`Merge-HwCertTestCollectionFromXml` cmdlet，以便合并这些测试结果；随后再将合并后的结果传递给`Export-HwCertTestCollectionToXml` cmdlet，最终将结果导出为`.xml`文件。

## 参数

### -Force
表示该 cmdlet 会解析 `.hckx` 包文件，然后替换任何现有的缓存 `.xml` 文件。

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

### -IncludeAll
如果指定了合并操作，那么合并将包括所有的测试结果，无论是通过还是失败的测试结果（例如那些标记为“未运行”的测试结果）。

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

### -LiteralPath
指定一个文件路径数组。这些文件路径指向.hckx格式的包文件。您必须具有对包含这些文件的文件夹的写入权限。

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
指定用于验证的测试集合.xml文件的路径。该cmdlet会将新的测试集合与验证集合进行比较，以确保至少存在一个验证结果。验证过程有助于确认从子实验室集合中合并的所有测试都符合原始测试集合的目标要求。

要获取用于验证的测试集合文件，请使用 **New-HwCertTestCollection** cmdlet 以及 **Export-HwCertTestCollectionToXml** cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[将HwCertTestCollection导出为XML文件](./Export-HwCertTestCollectionToXml.md)

[Merge-HwCertTestCollectionFromXml](./Merge-HwCertTestCollectionFromXml.md)

