---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: microsoft.windows.kits.hardware.certification.management.dll-Help.xml
Module Name: HardwareCertification
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hardwarecertification/import-hwcerttestcollectionfromxml?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-HwCertTestCollectionFromXml
---

# 从XML文件导入硬件证书测试集合

## 摘要
从.xml文件中导入一个测试集合。

## 语法

```
Import-HwCertTestCollectionFromXml [-LiteralPath] <String> [<CommonParameters>]
```

## 描述
`Import-HwCertTestCollectionFromXml` 这个 cmdlet 可以从 `.xml` 文件中导入测试集合。有关更多信息，请参阅微软开发者网络（MSDN）库中的 [Windows 硬件认证工具包下载](https://go.microsoft.com/fwlink/?LinkId=614978)。

在导入了一个测试集合后，你可以使用 **TestCollectionRecord** 的属性来对其进行过滤，然后使用 **Export-HwCertTestCollectionToXml** cmdlet 来导出过滤后的测试集合。

## 示例

### 示例 1：过滤测试集合
```
PS C:\> Import-HwCertTestCollectionFromXml -Input "C:\Temp\All.xml" | Where-Object { $_.ContentLevelSet.Contains("Basic") }
```

这个命令用于导入一个测试集合，然后找出属于指定内容级别的结果。该命令会导入一个名为“All.xml”的测试集合，并将其作为`TestCollectionRecord`对象；接着通过管道运算符将该对象传递给`Where-Object` cmdlet。`Where-Object` cmdlet会过滤导入的对象，以找出属于“Basic”内容级别的结果。有关更多信息，请输入`Get-Help Where-Object`。

#### 示例 2：过滤一个测试集，并将结果导出到一个新的测试集中
```
PS C:\> Import-HwCertTestCollectionFromXml -Input "C:\Temp\All.xml" | Where-Object { $_.ContentLevelSet.Contains("Basic") } | Export-HwCertTestCollectionToXml -Output "C:\Temp\Basic.xml"
```

此命令会导入一个测试集，查找属于指定内容级别的结果，并导出一个新的 `.xml` 文件，该文件仅包含这些结果。首先，命令将名为 `All.xml` 的测试集作为 `TestCollectionRecord` 对象导入系统，然后通过管道运算符将该对象传递给 `Where-Object` cmdlet。`Where-Object` cmdlet 会过滤导入的对象，以找出属于 “Basic” 内容级别的结果。有关更多信息，请输入 `Get-Help Where-Object`。随后，命令将这些结果传递给 `Export-HwCertTestCollectionToXml` cmdlet，该 cmdlet 将测试集导出到名为 `Basic.xml` 的文件中。

## 参数

### -LiteralPath
指定一个完整的路径。该路径指向测试集.xml文件的文件位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases: XML, Input, Path

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Export-HwCertTestCollectionToXml](./Export-HwCertTestCollectionToXml.md)

