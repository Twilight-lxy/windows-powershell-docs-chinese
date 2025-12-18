---
description: `Set-CIPolicySetting` cmdlet 用于修改代码完整性（Code Integrity）策略中的 `SecureSettings` 配置。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 10/20/2021
online version: https://learn.microsoft.com/powershell/module/configci/set-cipolicysetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-CIPolicySetting
---

# Set-CIPolicySetting

## 摘要
修改代码完整性策略中的安全设置（SecureSettings）。

## 语法

### 集合（Set）
```
Set-CIPolicySetting [-FilePath] <String> -Provider <String> -Key <String> -ValueName <String>
 -ValueType <String> -Value <String> [<CommonParameters>]
```

### 删除
```
Set-CIPolicySetting [-FilePath] <String> -Provider <String> -Key <String> -ValueName <String> [-Delete]
 [<CommonParameters>]
```

## 描述
`Set-CIPolicySetting` cmdlet 用于修改代码完整性（Code Integrity）策略中的安全设置。请指定需要修改的策略对应的 `.xml` 文件。Windows API 会通过这些安全设置来配置相应的安全行为。

## 示例

### 示例 1：设置代码完整性策略
```powershell
Set-CIPolicySetting -FilePath C:\Policies\WDAC_policy.xml -Key "{12345678-9abc-def0-1234-56789abcdef0}" -Provider WSH -Value $True -ValueName EnterpriseDefinedClsId -ValueType Boolean
```

此命令将代码完整性策略设置为允许使用指定的**提供者（Provider）**、**密钥（Key）**和**键名（ValueName）**。

## 参数

### -Delete
该cmdlet用于从代码完整性策略中删除一个安全设置，这些信息由**Provider**、**Key**和**ValueName**标识。

```yaml
Type: SwitchParameter
Parameter Sets: Delete
Aliases: d

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FilePath
指定 policy.xml 文件的完整路径。

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

### -Key
指定“安全设置”键（Secure Setting key）。该键是程序的 GUID，格式如下：

{33333333-4444-4444-1616-161616161616}

```yaml
Type: String
Parameter Sets: (All)
Aliases: k

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Provider
指定安全设置提供者（Secure Setting provider）。该提供者是指代码运行的平台。

```yaml
Type: String
Parameter Sets: (All)
Aliases: p

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Value
指定安全设置的值。可以使用 `$True` 来允许访问，或使用 `$False` 来拒绝访问。

仅对基础策略指定 `$False`（即拒绝该策略），而不适用于补充策略。

```yaml
Type: String
Parameter Sets: Set
Aliases: v

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ValueName
指定值名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: vn

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ValueType
指定值类型。有效值为：

- Boolean
- DWord
- Binary
- String

```yaml
Type: String
Parameter Sets: Set
Aliases: vt
Accepted values: Boolean, DWord, Binary, String

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[New-CIPolicy](New-CIPolicy.md)

[New-CIPolicyRule](New-CIPolicyRule.md)
