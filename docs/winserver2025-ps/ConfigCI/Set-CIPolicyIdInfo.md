---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/set-cipolicyidinfo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-CIPolicyIdInfo
---

# Set-CIPolicyIdInfo

## 摘要
修改代码完整性策略的名称和ID。

## 语法

```
Set-CIPolicyIdInfo [-FilePath] <String> [-PolicyName <String>] [-SupplementsBasePolicyID <Guid>]
 [-BasePolicyToSupplementPath <String>] [-ResetPolicyID] [-PolicyId <String>] [<CommonParameters>]
```

## 描述
`Set-CIPolicyIdInfo` cmdlet 用于修改代码完整性（Code Integrity）策略的名称和策略 ID。需要指定要修改的策略对应的 .xml 文件。Windows 事件跟踪（Event Tracing, ETW）会使用 `PolicyID` 和 `Name` 属性来识别当前在计算机上运行的策略。

## 示例

### 示例 1：修改策略的 ID 和名称
```
PS C:\> Set-CIPolicyIdInfo -FilePath ".\Policy03.xml" -PolicyId "CIP077" -PolicyName "CIPolicy03"
```

该命令会修改存储在 Policy03.xml 文件中的策略的策略ID和策略名称。

### 示例 2：修改策略的名称
```
PS C:\> Set-CIPolicyIdInfo -FilePath ".\Policy03.xml" -PolicyName "CIPolicy77"
```

此命令仅修改存储在Policy03.xml文件中的策略的名称。

### 示例 3：指定补充策略的基础策略 ID
```
PS C:\> Set-CIPolicyIdInfo -FilePath ".\Supplemental_Policy.xml" -BasePolicyToSupplementPath ".\Base_Policy.xml"
```

这个命令将从 Base_Policy.xml 文件中提取 PolicyID 字段，并修改 Supplementary_Policy.xml 文件中的 BasePolicyID 字段。

## 参数

### -BasePolicyToSupplementPath
指定基础策略的路径，以便获取补充策略的 **BasePolicyID** 属性的值。

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

### -PolicyId
指定 **PolicyID** 属性的值。该字符串不一定是 GUID（通用唯一标识符）。

```yaml
Type: String
Parameter Sets: (All)
Aliases: pid

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PolicyName
指定**Name**属性的值。

```yaml
Type: String
Parameter Sets: (All)
Aliases: pn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResetPolicyID
将 PolicyID 和 BasePolicyID 的值都重置为初始状态。该参数用于将采用单策略格式的保险政策转换为多策略格式。

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

### -SupplementsBasePolicyID
为补充策略指定 **BasePolicyID** 属性的值。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases: None

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-CIPolicyIdInfo](./Get-CIPolicyIdInfo.md)
