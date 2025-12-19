---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: microsoft.windows.kits.hardware.certification.management.dll-Help.xml
Module Name: HardwareCertification
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hardwarecertification/export-hwcerttestcollectiontoxml?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-HwCertTestCollectionToXml
---

# 将硬件证书测试集合导出为XML格式

## 摘要
将测试集合导出到.xml文件中。

## 语法

```
Export-HwCertTestCollectionToXml [-InputObject] <TestCollectionRecord[]> -Output <String>
 [-TestPassIdentifier <String>] [<CommonParameters>]
```

## 描述
`Export-HwCertTestCollectionToXml` cmdlet 将测试集合导出到 .xml 文件中。有关更多信息，请参阅微软开发者网络（MSDN）库中的 [Windows 硬件认证工具包下载](https://go.microsoft.com/fwlink/?LinkId=614978)。

在导出某个测试集合后，你可以使用 `Merge-HwCertTestCollectionFromXml` cmdlet 将它与其他测试集合合并。如果你之前已经导出了某些测试集合，可以使用 `Import-HwCertTestCollectionFromXml` cmdlet 将它们导入回来。导入测试集合后，可以通过 `TestCollectionRecord` 属性对其进行筛选，然后再使用该 cmdlet 将筛选后的测试集合重新导出。

## 示例

### 示例 1：过滤一个测试集合
```
PS C:\> Import-HwCertTestCollectionFromXml -Input "C:\Temp\All.xml" | Where-Object { $_.ContentLevelSet.Contains("Basic") } | Export-HwCertTestCollectionToXml -Output "C:\Temp\Basic.xml"
```

这个命令会导入一个测试集，找到属于指定内容级别的结果，然后导出一个新的 `.xml` 文件，其中仅包含这些结果。该命令使用 `Import-HwCertTestCollectionFromXml` cmdlet 将名为 `All.xml` 的测试集作为 `TestCollectionRecord` 对象导入进来，并通过管道运算符将该对象传递给 `Where-Object` cmdlet。`Where-Object` cmdlet 会过滤导入的对象，以找出属于 “Basic” 内容级别的结果。有关更多信息，请输入 `Get-Help Where-Object`。随后，这些结果会被传递给 `Export-HwCertTestCollectionToXml` cmdlet，该命令会将测试集导出到名为 `Basic.xml` 的文件中。

## 参数

### -InputObject
指定一个包含 **TestCollectionRecord** 对象的数组。要获取一个 **TestCollectionRecord** 对象，可以使用 **New-HwCertTestCollection** cmdlet。您还可以使用 **Merge-HwCertTestCollectionFromXml** 或 **Merge-HwCertTestCollectionFromPackage** cmdlet 来合并结果，并将其作为 **TestCollectionRecord** 对象获取。

```yaml
Type: TestCollectionRecord[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Output
指定导出文件的完整路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Path

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TestPassIdentifier
指定一个区分大小写的标识符，并将其分配给导出的测试集合。

```yaml
Type: String
Parameter Sets: (All)
Aliases: TP, ID

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Windows.Kits.Hardware.Certification.TestCollectionRecord

## 备注

## 相关链接

[从XML文件导入硬件证书测试集合](./Import-HwCertTestCollectionFromXml.md)

[New-HwCertTestCollection](./New-HwCertTestCollection.md)

[Merge-HwCertTestCollectionFromXml](./Merge-HwCertTestCollectionFromXml.md)

[Merge-HwCertTestCollectionFromPackage](./Merge-HwCertTestCollectionFromPackage.md)

