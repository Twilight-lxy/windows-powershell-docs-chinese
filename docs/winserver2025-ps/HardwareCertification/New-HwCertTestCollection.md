---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: microsoft.windows.kits.hardware.certification.management.dll-Help.xml
Module Name: HardwareCertification
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hardwarecertification/new-hwcerttestcollection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-HwCertTestCollection
---

# New-HwCertTestCollection

## 摘要
根据项目定义文件创建一个测试集合文件。

## 语法

```
New-HwCertTestCollection [-ProjectDefinitionFile] <String> [<CommonParameters>]
```

## 描述
`New-HwCertTestCollection` cmdlet 可以根据 Windows 硬件认证套件（HCK）项目定义文件创建一个测试集合文件。该集合文件用于表示由特定测试、目标系统及 Windows 操作系统版本组合而成的测试范围。有关更多信息，请参阅微软开发者网络（MSDN）库中的 [Windows 硬件认证套件下载](https://go.microsoft.com/fwlink/?LinkId=614978)。

您可以在测试工作流程的不同阶段以多种方式使用这个测试集文件，包括以下几种：

- Generate an initial test collection to understand the full scope of testing.
- Filter the test collection based on test metadata and properties, and then generate smaller collections for different labs to run.
- Use a test collection with results to control the scope of testing.
For instance, the tests could skip all passing tests.
- Use a test collection as a validation file when you merge test results from the smaller collections.

该 cmdlet 会创建临时项目和目标组件系列，以便枚举所有可能的测试用例。你可以通过使用 HCK 中提供的工具，在自动化工作流程之外重新利用这些生成的项目来进行额外的测试。

使用 **New-HwCertProjectDefinitionFile** cmdlet 来创建一个项目定义文件。

## 示例

### 示例 1：创建一个测试集合
```
PS C:\> New-HwCertTestCollection -ProjectDefinitionFile "C:\Temp\ProjectDefinitionWindows8Client.xml"
```

该命令根据名为ProjectDefinitionWindows8Client.xml的项目定义文件创建一个测试集合。

### 示例 2：创建一个测试集合并将其导出到文件中
```
PS C:\> New-HwCertTestCollection -ProjectDefinitionFile "C:\Temp\ProjectDefinitionWindows8Client.xml" | Export-HwCertTestCollectionToXml -Output "C:\Temp\TestCollectionWindows8Client.xml"
```

此命令会创建一个测试集合，然后将其导出到名为 `.xml` 的文件中。该命令根据名为 `ProjectDefinitionWindows8Client.xml` 的项目定义文件来生成这个测试集合，并通过管道运算符将该测试集合传递给 `Export-HwCertTestCollectionToXml` cmdlet。该 cmdlet 会将测试集合导出到一个名为 `TestCollectionWindows8Client.xml` 的文件中。

## 参数

### -ProjectDefinitionFile
使用完整的路径指定项目定义文件。要创建项目定义文件，请使用 **New-HwCertProjectDefinitionFile** cmdlet。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Input, PDF, Project

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Windows.Kits.Hardware.Certification.TestCollectionRecord

## 备注

## 相关链接

[将硬件证书测试集合导出为XML文件](./Export-HwCertTestCollectionToXml.md)

[New-HwCertProjectDefinitionFile](./New-HwCertProjectDefinitionFile.md)

