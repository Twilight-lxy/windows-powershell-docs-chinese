---
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
online version: https://learn.microsoft.com/powershell/module/hgsattestation/add-hgsattestationcipolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-HgsAttestationCIPolicy
---

# Add-HgsAttestationCIPolicy

## 摘要
授权可信的代码完整性策略可供主机使用，以验证 HGS（硬件安全模块）的安全性。

## 语法

### 控制台
```
Add-HgsAttestationCIPolicy [-InputObject] <Byte[]> -Name <String> [-PolicyVersion <PolicyVersion>] [-Stage]
 [-WhatIf] [-Confirm]
```

### 文件
```
Add-HgsAttestationCIPolicy [-Path] <String> [-Name <String>] [-PolicyVersion <PolicyVersion>] [-Stage]
 [-WhatIf] [-Confirm]
```

## 描述
`Add-HgsAttestationCIPolicy` cmdlet 根据一个受信任的代码完整性策略，为 HGS（Health Guarantee Service）添加相应的认证策略。当 HGS 配置为使用 TPM（Trusted Platform Module）进行认证时，主机需要使用已注册在 HGS 中的代码完整性策略之一才能成功通过认证过程。可以使用 `New-CIPolicy` 和 `ConvertFrom-CIPolicy` cmdlet 来创建一个二进制格式的代码完整性策略，并将其传递给 `Add-HgsAttestationCIPolicy` cmdlet。

HGS不会知道你的安全策略允许或禁止使用哪些软件，也不会了解策略中配置了哪些规则（例如强制执行的代码检查流程、重启操作等）。你应该为你的安全策略选择一个具有描述性的名称，这样在将来审查已授权的安全策略时，就能清楚地知道该策略所涵盖的范围。

## 示例

### 示例 1
```
PS C:\> Add-HgsAttestationCIPolicy -Path C:\temp\WS2016-Enforced.p7b -Name "Windows Server 2016 Enforced CI Policy"
```

将二进制代码完整性策略文件添加到 HGS（Hyper Graphics Service）中，并将该策略命名为“Windows Server 2016 强制执行的配置验证（CI）策略”。

## 参数

### -InputObject
字节数组，包含二进制代码完整性策略文件的内容。

```yaml
Type: Byte[]
Parameter Sets: Console
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
代码完整性政策的友好名称（简称）。

```yaml
Type: String
Parameter Sets: Console
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: File
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定包含代码完整性策略文件的路径，该文件以二进制形式存储。此类文件通常具有.p7b或.bin扩展名。

```yaml
Type: String
Parameter Sets: File
Aliases: FilePath, PSPath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PolicyVersion
保留以供将来使用。

```yaml
Type: PolicyVersion
Parameter Sets: (All)
Aliases:
Accepted values: None, PolicyVersion1503, PolicyVersion1704

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Stage
保留以供将来使用。

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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

## 输入

### Byte[]，System.String
此cmdlet接受一个代码完整性策略，该策略可以以**字节**数组的形式提供，也可以通过文件名传递。

## 输出

### AttestationPolicyInfo
此cmdlet返回身份验证策略信息。

## 备注

## 相关链接

