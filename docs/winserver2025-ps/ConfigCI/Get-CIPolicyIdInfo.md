---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/get-cipolicyidinfo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-CIPolicyIdInfo
---

# 获取CIPolicyId信息

## 摘要
显示代码完整性策略的相关信息。

## 语法

```
Get-CIPolicyIdInfo [-FilePath] <String> [<CommonParameters>]
```

## 描述
`Get-CIPolicyIdInfo` cmdlet 用于显示代码完整性（Code Integrity）策略的相关信息。你需要指定要修改的策略对应的 `.xml` 文件。

这个cmdlet返回的是人类可读的内容，并非用于与其他cmdlet配合使用。

## 示例

#### 示例 1：显示代码完整性策略信息
```
PS C:\> Get-CIPolicyIdInfo -FilePath ".\Policy03.xml"

Provider  : ConfigCIPolicy
Key       : PolicyInfo
ValueName : Name
ValueType : String
Value     : CIPolicy03

Provider  : ConfigCIPolicy
Key       : PolicyInfo
ValueName : PolicyId
ValueType : String
Value     : CIP077
```

此命令会显示存储在Policy03.xml文件中的代码完整性策略的相关信息。该策略同时具有“名称”和“ID”这两个属性的值。

## 参数

### -FilePath
指定代码完整性策略（Code Integrity policy）的.xml文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: f

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### CIPolicyIdInfo

## 备注

## 相关链接

[Set-CIPolicyIdInfo](./Set-CIPolicyIdInfo.md)

