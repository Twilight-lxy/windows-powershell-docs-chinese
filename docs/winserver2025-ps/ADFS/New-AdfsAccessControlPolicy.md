---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/new-adfsaccesscontrolpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AdfsAccessControlPolicy
---

# 新的 AdfsAccessControlPolicy

## 摘要
创建一个 AD FS 访问控制策略。

## 语法

```
New-AdfsAccessControlPolicy -Name <String> [-SourceName <String>] [-Identifier <String>]
 [-Description <String>] [-PolicyMetadata <PolicyMetadata>] [-PolicyMetadataFile <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`New-AdfsAccessControlPolicy` cmdlet 可以根据策略元数据文件创建一个 Active Directory Federation Services (AD FS) 访问控制策略。

**如何创建联邦元数据文件**

联邦元数据文档是一个XML文件，可以通过[此处下载](/windows-server/identity/ad-fs/operations/offline-tools)获取。要下载该文件，请输入您的联邦服务名称，然后选择“获取联邦元数据”按钮。

## 示例

#### 示例 1：从策略元数据文件创建策略模板
```
PS C:\> $t=New-AdfsAccessControlPolicy -Name "DemoOne" -PolicyMetadataFile "C:\filepath\ PolicyTemplateIntranetWithOneGroupParameterMFA.xml"
```

该命令根据一个策略元数据文件创建一个策略模板。

### 示例 2：使用策略模板创建一个依赖方
```
PS C:\> Add-AdfsRelyingPartyTrust -Name "DemoRP1" -Identifier "https://DemoRP1" -AccessControlPolicyName DemoOne -AccessControlPolicyParameters "Administrators"
```

该命令使用策略模板创建一个依赖方（relying party）。

### 示例 3：修改参数
```
PS C:\> Set-AdfsRelyingPartyTrust -TargetName "DemoRP1" -AccessControlPolicyParameters ("Administrators","Users") -AccessControlPolicyName "DemoOne"
```

此命令用于修改访问控制策略的参数。

### 示例 4：取消对策略模板的分配
```
PS C:\> Set-AdfsRelyingPartyTrust -TargetName "DemoRP1" -AccessControlPolicyName $null
```

此命令用于取消将某个策略模板分配给特定对象的操作（即解除绑定）。

### 示例 5：从现有的模板创建一个策略模板
```
PS C:\> New-AdfsAccessControlPolicy -Name "DemoCopyOne" -SourceName "DemoOne"
```

该命令根据现有的模板创建一个新的策略模板。

### 示例 6：根据现有的元数据创建一个策略模板
```
PS C:\> New-AdfsAccessControlPolicy -Name "DemoCopyTwo" -PolicyMetadata $t.PolicyMetadata
```

这个命令会根据现有的元数据创建一个策略模板。$t变量是一个来自**New-AccessControlPolicy**的对象。

### 示例 7：根据依赖方结果策略创建政策模板
```
PS C:\> New-AdfsAccessControlPolicy -Name "DemoCopyWithAssignment" -PolicyMetadata $r.ResultantPolicy
```

该命令根据依赖方结果策略创建一个策略模板。变量 `$r` 是通过 `Get-AdfsRelyingPartyTrust` 命令返回的对象。

### 示例 8：将依赖方更改为使用新的模板
```
PS C:\> Set-AdfsRelyingPartyTrust -TargetName "DemoRP1" -AccessControlPolicyName "DemoTwo" -AccessControlPolicyParameters @{PermitGroup="Users";RejectGroup="Administrators"}
```

这个命令会更改依赖方所使用的模板，使其使用一个新的模板。

### 示例 9：包含具体要求的复杂条件
```
PS C:\> Set-AdfsRelyingPartyTrust -TargetName "DemoRP1" -AccessControlPolicyName DemoRP -AccessControlPolicyParameters`
    @{"SPParameter"= @{ClaimType="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/OfficeLocation"; Operator="Equals"; Value="Redmond"}}
```

### 示例 10：针对单个参数的两个具体声明
```
PS C:\> Set-AdfsRelyingPartyTrust -TargetName "DemoRP1" -AccessControlPolicyName "DemoRP" -AccessControlPolicyParameters`
    @{"SPParameter"= (@{ClaimType="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/OfficeLocation"; Operator="Equals"; Value=("Redmond","DC")},`
                      @{ClaimType="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/Department"; Operator="Equals"; Value="Azure"})}
```

## 参数

### -Description
指定一个描述信息。

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

### -Identifier
指定一个ID。

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

### -Name
指定一个名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PolicyMetadata
为策略指定元数据。

```yaml
Type: PolicyMetadata
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PolicyMetadataFile
指定一个包含策略元数据的文件。

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

### -SourceName
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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AdfsAccessControlPolicy](./Get-AdfsAccessControlPolicy.md)

[Remove-AdfsAccessControlPolicy](./Remove-AdfsAccessControlPolicy.md)

[Set-AdfsAccessControlPolicy](./Set-AdfsAccessControlPolicy.md)

