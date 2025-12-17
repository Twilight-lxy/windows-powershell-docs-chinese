---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/new-adfsclaimruleset?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AdfsClaimRuleSet
---

# 新的 AdfsClaimRuleSet

## 摘要
创建一组声明规则（claim rules）。

## 语法

### FromParams
```
New-AdfsClaimRuleSet -ClaimRule <String[]> [<CommonParameters>]
```

### FromFile
```
New-AdfsClaimRuleSet -ClaimRuleFile <String> [<CommonParameters>]
```

## 描述
`New-AdfsClaimRuleSet` cmdlet 在 Active Directory Federation Services (AD FS) 2.0 中创建一组声明规则。

## 示例

### 示例 1：使用文本文件创建一个声明规则集
```
PS C:\> $RuleSet = New-AdfsClaimRuleSet -ClaimRuleFile 'C:\ruleset.txt'
PS C:\> Set-AdfsRelyingPartyTrust -TargetName "Fabrikam" -IssuanceTransformRules $RuleSet.ClaimRulesString
```

第一个命令通过使用一个文本文件来创建一个声明规则集（claim rule set），然后将其存储在 `$RuleSet` 变量中。

第二个命令使用了 **Set-AdfsRelyingPartyTrust** cmdlet，将存储在 `$RuleSet` 中的规则集分配给一个依赖方信任（relying party trust）。该命令引用了存储在 `$RuleSet` 中的对象的 **ClaimsRuleString** 属性。

### 示例 2：使用内联规则创建声明规则集
```
PS C:\> $RuleSet = New-AdfsClaimRuleSet -ClaimRule 'c:[] => issue(claim = c);'
PS C:\> Set-AdfsRelyingPartyTrust -TargetName "Fabrikam" -IssuanceTransformRules $RuleSet.ClaimRulesString
```

第一个命令使用内联的 AD FS 2.0 声明语言规则来创建一个声明规则集，然后将其存储在 `$RuleSet` 变量中。

第二个命令使用 `Set-AdfsRelyingPartyTrust` 将存储在 `$RuleSet` 中的规则集分配给一个依赖方信任关系（relying party trust）。该命令引用了存储在 `$RuleSet` 中的对象的 `ClaimsRuleString` 属性。

## 参数

### -ClaimRule
在这个规则集中，指定了一组单独的规则。

```yaml
Type: String[]
Parameter Sets: FromParams
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClaimRuleFile
指定由规则集中的所有规则共同生成的序列化策略文本。

```yaml
Type: String
Parameter Sets: FromFile
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### MicrosoftIdentityServer.PowerShellResources.ClaimRuleSet
这个cmdlet生成一个类结构，用于表示一组AD FS 2.0声明规则。

## 备注
* You can assign these claim rules to a claims provider trust or relying party trust by using the corresponding cmdlets.

## 相关链接

[Get-AdfsClaimsProviderTrust](./Get-AdfsClaimsProviderTrust.md)

[Set-AdfsClaimsProviderTrust](./Set-AdfsClaimsProviderTrust.md)

[更新 AdfsClaimsProviderTrust](./Update-AdfsClaimsProviderTrust.md)

[Set-AdfsRelyingPartyTrust](./Set-AdfsRelyingPartyTrust.md)

