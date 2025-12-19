---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: microsoft.windows.kits.hardware.certification.management.dll-Help.xml
Module Name: HardwareCertification
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hardwarecertification/new-hwcerttestcollectionexcelreport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-HwCertTestCollectionExcelReport
---

# New-HwCertTestCollectionExcelReport

## 摘要
生成一份HCK测试总结报告。

## 语法

```
New-HwCertTestCollectionExcelReport [-LiteralPath] <String[]> -ExcelPath <String> -ResultCount <Int32>
 [<CommonParameters>]
```

## 描述
`New-HwCertTestCollectionExcelReport` cmdlet 用于将 Windows 硬件认证套件（HCK）的测试汇总报告生成为 Microsoft Excel 工作簿。你需要指定一个或多个合并后的测试集合 `.xml` 文件。该 cmdlet 会为每个合并后的测试集合文件创建一个单独的工作表，汇总各文件中的测试结果，并在汇总报告中对比针对同一测试目标的测试结果。汇总报告显示总通过次数、符合特定过滤条件的通过次数、失败次数以及 N-1 回归数据（即与之前版本相比的变化情况）。有关更多信息，请参阅 Microsoft 开发者网络（MSDN）库中的 [Windows 硬件认证套件下载](https://go.microsoft.com/fwlink/?LinkId=614978)。

在测试结果汇总过程中，每次测试最多可以使用十个测试结果。最新的通过结果将被优先作为汇总结果。

摘要报告中的测试集合最大数量为八个。如果您指定了一个合并后的测试集合，那么报告将仅包含该测试通过的总结信息，而不会进行N-1次回归比较。

要创建合并后的测试结果收集文件，请使用 `Merge-HwCertTestCollectionFromPackage` 和 `Merge-HwCertTestCollectionFromXml` 这两个 cmdlet，以及 `Export-HwCertTestCollectionToXml` cmdlet。

## 示例

#### 示例 1：为两个合并后的测试集合生成报告
```
PS C:\> New-HwCertTestCollectionExcelReport -LiteralPath ("C:\Temp\Merged_TP001.xml", "C:\Temp\Merged_TP002.xml") -ExcelPath "C:\Temp\Report.xls" -ResultCount 1
```

该命令从两个测试通过过程中生成的合并后的 `.xml` 文件中生成一份 Excel 报告。命令指定了报告的副本数量为 1（即只生成一份报告）。

## 参数

### -ExcelPath
为新Excel报告指定一个完整路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LiteralPath
指定一个包含完整路径的数组。这些路径指向被合并到的测试集合.xml文件。您最多可以指定8个文件。

该cmdlet根据此参数中文件的顺序来确定N-1回归数据比较的顺序。例如，第二个文件会与第一个文件进行比较，第三个文件则会与第二个文件进行比较。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: Input, MergedCollection

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResultCount
用于指定结果的数量。该cmdlet会报告这些结果，并在结果汇总过程中使用这些数据。最大值为10。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Merge-HwCertTestCollectionFromPackage](./Merge-HwCertTestCollectionFromPackage.md)

[Merge-HwCertTestCollectionFromXml](./Merge-HwCertTestCollectionFromXml.md)

[将HwCertTest集合导出为XML](./Export-HwCertTestCollectionToXml.md)

