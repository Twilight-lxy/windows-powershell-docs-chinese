---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BestPractices.Cmdlets.dll-Help.xml
Module Name: BestPractices
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/bestpractices/get-bparesult?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-BpaResult
---

# Get-BpaResult

## 摘要
检索并显示针对特定模型的最新最佳实践分析器（Best Practices Analyzer，简称BPA）扫描的结果。

## 语法

### ModelParameterSet（默认值）
```
Get-BpaResult [-ModelId] <String> [-CollectedConfiguration] [-All] [-Filter <FilterOptions>]
 [-RepositoryPath <String>] [<CommonParameters>]
```

### SubModelParameterSet
```
Get-BpaResult [-ModelId] <String> [-CollectedConfiguration] [-All] [-Filter <FilterOptions>]
 [-RepositoryPath <String>] [-SubModelId <String>] [-ComputerName <String[]>] [-Context <String>]
 [<CommonParameters>]
```

## 描述
`Get-BpaResult` cmdlet 用于检索并显示安装在计算机上的特定模型的最新最佳实践分析器（Best Practices Analyzer，简称 BPA）扫描结果。要使用此 cmdlet，需要添加 `ModelId` 参数，并指定要查看其最新 BPA 扫描结果的模型标识符（ID）。也可以使用 `All` 参数来获取该模型的所有扫描结果；如果未指定 `All` 参数，则仅返回该模型的最新扫描结果。

此cmdlet可用于查看针对特定模型的BPA扫描结果。管理员需要提供一个模型ID作为参数，系统便会显示该模型的最新扫描结果。

注意：此cmdlet不会启动新的BPA扫描（Business Process Analysis）。

## 示例

### 示例 1：通过模型 ID 获取 BPA 扫描结果
```
PS C:\> Get-BPAResult -ModelId ModelId1
```

这个示例返回了由 ModelId1 表示的模型最新的 BPA 扫描结果。也可以使用 *ModelId* 参数的简写形式，即 *Id*。

### 示例 2：获取所有 BPA 模型扫描结果
```
PS C:\> Get-BPAModel | Get-BPAResult
```

在这个例子中，使用了 `Get-BpaModel` cmdlet 来获取安装在计算机上的所有 BPA（Business Process Automation）模型的列表。`Get-BpaModel` cmdlet 的输出结果被传递给另一个 cmdlet，以便检索所有受 BPA 支持的模型最新的扫描结果。

## 参数

### -All
返回报表的输出类型。该参数可用于检索特定模型的所有扫描结果。如果未指定此参数，则会返回该模型最新的扫描结果。

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

### -CollectedConfiguration
仅返回在 BPA 扫描过程中收集到的发现信息，而不包括模型中规则评估的结果。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定用于获取 BPA 结果的目标计算机。

```yaml
Type: String[]
Parameter Sets: SubModelParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Context
在特定模型的背景下扫描子模型（该模型与子模型的父模型不同）。例如，管理员希望对SQL模型的“Backend”子模型进行扫描，但仅限于在第三个模型的上下文中进行扫描；这个第三个模型是一种依赖于SQL Server的技术。

```yaml
Type: String
Parameter Sets: SubModelParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Filter
用于过滤返回结果的类型。该参数的可接受值包括：

- All
- Compliant
- Noncompliant

```yaml
Type: FilterOptions
Parameter Sets: (All)
Aliases:
Accepted values: All, Compliant, Noncompliant

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ModelId
确定需要从中获取结果的模型。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Id, BestPracticesModelId

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -RepositoryPath
指定用于获取由 `Invoke-BpaModel` 命令生成的结果的仓库位置。`Invoke-BpaModel` cmdlet 提供了一个选项，可以将结果存储在 `ReportsRoot` 注册表键中指定的默认报告仓库位置，或者存储在该参数值所指定的自定义位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SubModelId
该函数用于识别由 *ModelId* 参数指定的模型的子模型。例如，Update Services 模型（`Microsoft/Windows/UpdateServices`）有两个子模型（UpdateServices-DB 和 UpdateServices-Services）。

```yaml
Type: String
Parameter Sets: SubModelParameterSet
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

### System.String

## 输出

### Microsoft.BestPractices.CoreInterfaceReport

### Microsoft.BestPractices.CoreInterface Result

## 备注

## 相关链接

[Get-BpaModel](./Get-BpaModel.md)

[Invoke-BpaModel](./Invoke-BpaModel.md)

[Set-BpaResult](./Set-BpaResult.md)

