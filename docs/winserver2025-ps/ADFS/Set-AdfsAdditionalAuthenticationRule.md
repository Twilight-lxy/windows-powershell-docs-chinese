---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsadditionalauthenticationrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsAdditionalAuthenticationRule
---

# 设置 AdfsAdditionalAuthenticationRule 规则

## 摘要
设置全局规则，这些规则会触发其他身份验证提供者的调用。

## 语法

### 规则集（默认设置）
```
Set-AdfsAdditionalAuthenticationRule [-AdditionalAuthenticationRules] <String> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### RuleSetFile
```
Set-AdfsAdditionalAuthenticationRule [-AdditionalAuthenticationRulesFile] <String> [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsAdditionalAuthenticationRule` cmdlet 用于设置全局规则，这些规则会触发额外身份验证提供程序的调用。当声明引擎评估这些额外身份验证规则并确定需要进行多因素身份验证时，系统会提示用户执行额外的身份验证流程。您可以以声明规则字符串的形式指定这些规则，或者指定一个包含声明规则的文件来配置这些规则。

仅当您的所有应用程序都能够通过 Active Directory Federation Services (AD FS) 来执行基于 Web 的凭据收集时，才使用此规则。如果规则评估的结果为“true”，那么使用 WS-Trust 等协议的应用程序将无法获取安全令牌。

您还可以使用 `Set-AdfsRelyingPartyTrust` cmdlet 和 `AdditionalAuthenticationRule` 参数，为各个依赖方信任设置规则。

## 示例

### 示例 1：设置一条全局性的额外认证规则
```
PS C:\> Set-AdfsAdditionalAuthenticationRule -AdditionalAuthenticationRules 'c:[type == "http://schemas.microsoft.com/ws/2012/01/insidecorporatenetwork", value == "false"] => issue(type = "http://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationmethod", value = "http://schemas.microsoft.com/claims/multipleauthn" );'
```

此命令设置了一条额外的身份验证规则，要求使用多因素认证（multi-factor authentication）。

## 参数

### -AdditionalAuthenticationRules
用于指定附加身份验证的规则。有关这些规则的声明语言（claims language）的更多信息，请参阅 TechNet 上的 [Understanding Claim Rule Language in AD FS 2.0 & Higher](https://social.technet.microsoft.com/wiki/contents/articles/4792.understanding-claim-rule-language-in-ad-fs-2-0-higher.aspx)。

```yaml
Type: String
Parameter Sets: RuleSets
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -AdditionalAuthenticationRulesFile
指定一个包含声明规则的文本文件的完全限定路径（即包含文件所在目录和文件名的完整路径）。

```yaml
Type: String
Parameter Sets: RuleSetFile
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AdfsAdditionalAuthenticationRule](./Get-AdfsAdditionalAuthenticationRule.md)

