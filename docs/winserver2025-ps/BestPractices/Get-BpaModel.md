---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BestPractices.Cmdlets.dll-Help.xml
Module Name: BestPractices
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/bestpractices/get-bpamodel?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-BpaModel
---

# Get-BpaModel

## 摘要
检索并显示系统上安装的所有BPA（Business Process Analysis）模型列表。

## 语法

### BPANoFilterParameterSet（默认值）
```
Get-BpaModel [-RepositoryPath <String>] [<CommonParameters>]
```

### BPAFilterParameterSet
```
Get-BpaModel [-ModelId] <String[]> [[-SubModelId] <String>] [-RepositoryPath <String>] [<CommonParameters>]
```

## 描述
`Get-BpaModel` cmdlet 可以检索并显示计算机上安装的最佳实践分析器（Best Practices Analyzer，简称 BPA）所支持的模型列表。

如果未指定任何参数，此 cmdlet 将返回计算机上安装的所有模型。如果使用 *ModelId* 参数指定了某个模型，则会返回该指定的模型。

## 示例

### 示例 1：通过 ID 获取 BPA 模型
```
PS C:\> Get-BPAModel -ModelId "ADRMS"

Id                     : Microsoft/Windows/ADRMS
Company                : Microsoft Corporation
Name                   : RightsManagementServices
Version                : 1.0
LastScanTime           : Never
LastScanTimeUtcOffset  :
SubModels              :
Parameters             :
ModelType              : SingleMachine
SupportedConfiguration :
```

这个示例可以用来获取在 *ModelId* 参数中指定的 BPA 模型的详细信息，该模型由 ModelID1 代表。也可以使用 *ModelId* 参数的缩写形式 *Id*。

### 示例 2：获取所有 BPA 模型
```
PS C:\> Get-BPAModel

Id                       Last Scan Time
---                      --------------
ModelID1                 01/05/2012 10:12
ModelID2                 Never
ModelID3                 05/20/2010 12:46
```

这个示例可以用来获取计算机上安装的所有模型的BPA扫描详细信息。

## 参数

### -ModelId
用于指定BPA模型的ID，以便显示该模型的详细信息。也可以使用该参数的缩写形式“*Id*”。这个ID标识了需要获取其详细信息的模型。

```yaml
Type: String[]
Parameter Sets: BPAFilterParameterSet
Aliases: Id, BestPracticesModelId

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -RepositoryPath
指定用于获取由 **Invoke-BpaModel** cmdlet 生成的结果的仓库位置。**Invoke-BpaModel** 提供了一个选项，可以将结果存储在默认的报告仓库位置（该位置由 ReportsRoot 注册表键标识），或者存储在通过此参数传递给 **Invoke-BpaModel** cmdlet 的自定义位置中。

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
用于确定根据 *ModelId* 参数指定的模型所对应的子模型。例如，Update Services 模型（`Microsoft/Windows/UpdateServices`）包含两个子模型（`UpdateServices-DB` 和 `UpdateServices-Services`）。

```yaml
Type: String
Parameter Sets: BPAFilterParameterSet
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.BestPractices.CoreInterface.Model

## 备注

## 相关链接

[Get-BpaResult](./Get-BpaResult.md)

[Invoke-BpaModel](./Invoke-BpaModel.md)

[Set-BpaResult](./Set-BpaResult.md)

