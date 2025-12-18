---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/add-signerrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-SignerRule
---

# Add-SignerRule

## 摘要
创建一个签名者规则，并将其添加到策略中。

## 语法

### 证书
```
Add-SignerRule -FilePath <String> -CertificatePath <String> [-Kernel] [-User] [-Update] [-Supplemental] [-Deny]
 [<CommonParameters>]
```

### CertStore
```
Add-SignerRule -FilePath <String> -CertStorePath <String> [-Kernel] [-User] [-Update] [-Supplemental] [-Deny]
 [<CommonParameters>]
```

## 描述
`Add-SignerRule` cmdlet 根据证书创建一个签名规则，然后将该规则添加到代码完整性策略中。默认情况下，此 cmdlet 创建的是允许（allow）类型的规则。请从以下场景中为该规则在策略中指定至少一种应用场景：

- User
- Kernel
- Update

## 示例

### Example 1: Create and add a signer rule for User mode
```
PS C:\> Add-SignerRule -FilePath '.\Policy.xml' -CertificatePath '.\certificate07.cer' -User
```

This command generates a signer rule for the certificate in certificate07.cer.
The command adds the rule to policy.xml for the User mode scenario.

## 参数

### -CertificatePath
Specifies the path of a certificate (.cer) file that this cmdlet uses for the rule.

```yaml
Type: String
Parameter Sets: Certificate
Aliases: c

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertStorePath
Specifies the path to a certificate store to export certificates into the policy.

```yaml
Type: String
Parameter Sets: CertStore
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Deny
Indicates that this cmdlet creates a deny rule instead of the default allow rule.

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

### -FilePath
Specifies the path of the policy .xml file to which this cmdlet adds the rule.

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

### -Kernel
Indicates that this cmdlet adds the rule as a Kernel mode rule.
You can add a rule as more than one scenario.

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

### -Supplemental
Indicates that this cmdlet adds the rule as a Supplemental policy signers rule.
You can add a rule as more than one scenario.

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

### -Update
Indicates that this cmdlet adds the rule as an Update policy signers rule.
You can add a rule as more than one scenario.

Update policy signers rules to determine which signers can sign a policy in signed policy scenario.

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

### -User
Indicates that this cmdlet adds the rule as a User mode rule.
You can add a rule as more than one scenario.

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[New-CIPolicyRule](./New-CIPolicyRule.md)

