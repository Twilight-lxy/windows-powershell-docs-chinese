---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/edit-cipolicyrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Edit-CIPolicyRule
---

# 修改 CIPolicyRule

## 摘要
此cmdlet不受支持。

## 语法

### FileRule
```
Edit-CIPolicyRule [-Id] <String> [-Name <String>] [-RType <String>] [-FileName <String>] [-Version <String>]
 [-HashPath <String>] -FilePath <String> [<CommonParameters>]
```

### SignerRule
```
Edit-CIPolicyRule [-Id] <String> [-Name <String>] [-RType <String>] [-Root <String>] [-AddEkus <String[]>]
 [-RemoveEkus <String[]>] [-Issuer <String>] [-Publisher <String>] [-OemId <String>]
 [-AddExceptions <String[]>] [-RemoveExceptions <String[]>] -FilePath <String> [<CommonParameters>]
```

## 描述
`Edit-CIPolicyRule` cmdlet 不受支持，请不要使用此 cmdlet。

## 示例


## 参数

### -AddEkus


```yaml
Type: String[]
Parameter Sets: SignerRule
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AddExceptions


```yaml
Type: String[]
Parameter Sets: SignerRule
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FileName


```yaml
Type: String
Parameter Sets: FileRule
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FilePath


```yaml
Type: String
Parameter Sets: (All)
Aliases: f

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HashPath


```yaml
Type: String
Parameter Sets: FileRule
Aliases: h

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Id


```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Issuer


```yaml
Type: String
Parameter Sets: SignerRule
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name


```yaml
Type: String
Parameter Sets: (All)
Aliases: n

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OemId


```yaml
Type: String
Parameter Sets: SignerRule
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Publisher
```yaml
Type: String
Parameter Sets: SignerRule
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoveEkus

```yaml
Type: String[]
Parameter Sets: SignerRule
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoveExceptions

```yaml
Type: String[]
Parameter Sets: SignerRule
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Root

```yaml
Type: String
Parameter Sets: SignerRule
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RType
```yaml
Type: String
Parameter Sets: (All)
Aliases: t
Accepted values: Allow, Deny, a, d

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Version


```yaml
Type: String
Parameter Sets: FileRule
Aliases: v

Required: False
Position: Named
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

