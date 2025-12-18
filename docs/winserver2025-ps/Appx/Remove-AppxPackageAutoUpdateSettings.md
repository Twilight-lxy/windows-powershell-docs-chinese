---
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: appx
online version: https://go.microsoft.com/fwlink/?LinkId=246400
schema: 2.0.0
title: Remove-AppxPackageAutoUpdateSettings
---

# 移除 AppxPackage 的自动更新设置

## 摘要
删除为特定Windows应用程序配置的设置。

## 语法

```
Remove-AppxPackageAutoUpdateSettings [-PackageFamilyName] <String> [-UseSystemPolicySource] [-AllUsers]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AppxPackageAutoUpdateSettings` 这个 PowerShell cmdlet 用于删除为特定的或所有已安装的 Windows 应用程序配置的与自动更新和修复相关的设置。

## 示例

### 示例 1
```powershell
PS C:\> Remove-AppxPackageAutoUpdateSettings -PackageFullName publisher.package1_1.0.0.0_neutral__8wekyb3d8bbwe
```

这个示例会移除已安装并注册到当前登录用户的某个特定Windows应用程序的“自动更新”和“自动修复”设置。

## 参数

### -AllUsers
{{ 填充所有用户信息 的描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PackageFamilyName
{{ 填写 PackageFamilyName 和 Description }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -UseSystemPolicySource
{{ 填写 UseSystemPolicySource 的描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
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
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object
## 备注

## 相关链接
