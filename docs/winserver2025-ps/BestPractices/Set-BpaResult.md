---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BestPractices.Cmdlets.dll-Help.xml
Module Name: BestPractices
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/bestpractices/set-bparesult?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-BpaResult
---

# Set-BpaResult

## 摘要
可以选择排除或包含BPA扫描的现有结果，从而仅显示指定的扫描结果。

## 语法

```
Set-BpaResult [[-Exclude] <Boolean>]
 [-Results] <System.Collections.Generic.List`1[Microsoft.BestPractices.CoreInterface.Result]>
 [[-RepositoryPath] <String>] [<CommonParameters>]
```

## 描述
`Set-BPAResult` 这个 cmdlet 可以排除或包含 Best Practices Analyzer (BPA) 扫描的现有结果，从而仅显示指定的扫描结果。该 cmdlet 中指定的操作（例如 `Exclude`）决定了如何更新 BPA 扫描的现有结果。通常在使用 `Get-BpaResult` cmdlet 获取扫描结果集之后，才会应用这个 cmdlet。可以对 `Get-BpaResult` 返回的结果进行过滤，然后将过滤后的结果集通过管道传递给 `Set-BPAResult` cmdlet，并指定是包含这些过滤后的结果还是排除它们。

这将使用指定的结果集合和指定的操作来更新结果文件中的内容。通常情况下，管理员需要先调用 **Get-BpaResult** cmdlet 来获取结果集合，然后应用一些筛选条件，并将该集合通过管道传递给此 cmdlet，同时指定所需的操作（排除或包含）。

如果此 cmdlet 在结果被写入文件之前被取消，那么操作将会被终止，并且结果文件不会被修改。如果在结果文件已经被修改之后才发生取消操作，那么 cmdlet 的相应操作仍会继续执行，此时该 cmdlet 无法再被取消。

## 示例

### 示例 1：从 BPA 扫描中排除过滤后的结果
```
PS C:\> Get-BPAResult -ModelId "ModelId1" | Where-Object -FilterScript { $_.Category -Eq "Performance" } | Set-BPAResult -ModelId "ModelId1" -Exclude $True
```

This example, to the left of the first pipeline operator (`|`), uses the **Get-BpaResult** cmdlet to retrieve BPA scan results for the model ID represented by ModelId1.
The second section of the cmdlet filters the results of **Get-BpaResult** to get only those scan results for which the category name is equal to Performance.
The final section of the example, following the second pipeline operator, excludes the Performance results filtered by the previous section of the example.

### 示例 2：使用变量从 BPA 扫描结果中排除被过滤的数据
```
The $rcPolicy variable is created to store the filtered results of **Get-BpaResult**; this variable can be used in subsequent cmdlets to represent those results.
PS C:\> $rcPolicy = Get-BPAResult -ModelId ModelId1 | Where-Object -FilterScript { $_.Category -Eq "Policy" }

The second line of the example uses this cmdlet to exclude the set of results stored in the $rcPolicy variable, for the specified model ID. In this cmdlet, the *Results* parameter is added because the administrator wants to exclude a specific subset of scan results for that model, and has created the variable $rcPolicy to represent that subset of results.
PS C:\> Set-BPAResult -ModelId "ModelId1" -Exclude $True -Results $rcPolicy
```

This example, to the left of the pipeline operator (`|`), instructs the **Get-BpaResult** cmdlet to retrieve BPA scan results for the model represented by ModelId1.
The second section of the example, after the pipeline, filters the results of **Get-BpaResult** to return only those scan results for which the category name is equal to (note the Eq comparison operator) Policy.

## 参数

### -Exclude
此命令会移除通过添加到该 cmdlet 中的过滤器所指定的所有 BPA（ Bisphenol A，双酚 A）扫描结果。` Exclude` 操作适用于该 cmdlet 返回的所有结果。要使用此参数排除某些结果，请在参数后添加 `$True`，例如：`-Exclude $True`

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RepositoryPath
指定报告应存储的位置。`Invoke-BpaModel` cmdlet 提供了一个选项，可以将结果存储在由 `ReportsRoot` 注册表键引用的默认报告存储位置中，或者存储在作为该参数输入的自定义位置中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Results
指定需要在此cmdlet返回的结果文件中更新的结果集合。此参数通常用于指代已经存储在变量中的经过过滤的扫描结果子集；该变量的名称即为该参数的有效值。这就是需要在结果文件中更新的结果集合。例如，如果创建了一个名为 `$allPerformance` 的变量来存储对计算机上所有角色进行的BPA扫描的所有“性能”类别的结果，并希望将这些“性能”结果从完整的扫描结果集合中排除出去，那么可以在此cmdlet中添加以下参数：`-Results $allPerformance`

```yaml
Type: System.Collections.Generic.List`1[Microsoft.BestPractices.CoreInterface.Result]
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Collections.Generic.List<Microsoft.BestPractices.CoreInterface.Result>
由*Results*参数指定的输入对象。

## 输出

### 无

## 备注

## 相关链接

[Get-BpaModel](./Get-BpaModel.md)

[Get-BpaResult](./Get-BpaResult.md)

[Invoke-BpaModel](./ Invoke-BpaModel.md)

[Where-对象](https://go.microsoft.com/fwlink/?LinkID=113423)

