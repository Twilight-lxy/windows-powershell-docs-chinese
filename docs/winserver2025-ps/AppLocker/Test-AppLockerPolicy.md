---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Security.ApplicationId.PolicyManagement.Cmdlets.dll-Help.xml
Module Name: AppLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/applocker/test-applockerpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-AppLockerPolicy
---

# 测试 AppLockerPolicy

## 摘要
指定 AppLocker 策略，以确定给定用户是否被允许运行输入文件。

## 语法

### ByXmlPolicy（默认值）
```
Test-AppLockerPolicy [-XmlPolicy] <String> -Path <System.Collections.Generic.List`1[System.String]>
 [-User <String>]
 [-Filter <System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.PolicyDecision]>]
 [<CommonParameters>]
```

### ByXmlPolicyAppx
```
Test-AppLockerPolicy [-XmlPolicy] <String>
 -Packages <System.Collections.Generic.List`1[Microsoft.Windows.Appx.PackageManager.Commands.AppxPackage]>
 [-User <String>]
 [-Filter <System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.PolicyDecision]>]
 [<CommonParameters>]
```

### ByPolicyObject
```
Test-AppLockerPolicy [-PolicyObject] <AppLockerPolicy> -Path <System.Collections.Generic.List`1[System.String]>
 [-User <String>]
 [-Filter <System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.PolicyDecision]>]
 [<CommonParameters>]
```

## 描述
`Test-AppLockerPolicy` cmdlet 用于指定 AppLocker 策略，以确定是否允许特定用户在一台本地计算机上运行一组文件。

要测试 AppLocker 规则对嵌套组的作用，需要为 *User* 参数指定该嵌套组中的一个代表性成员。例如，如果将 *User* 参数设置为“Everyone”组（即所有用户），那么允许 Everyone 组运行 calc.exe 的规则可能无法正确生效。在这种情况下，应该为 *User* 参数指定 Finance 组中的一个代表性成员。

## 示例

### 示例 1：如果允许程序运行，则生成报告
```
PS C:\> Test-AppLockerPolicy -XMLPolicy C:\Policy.xml -Path c:\windows\system32\calc.exe, C:\windows\system32\notepad.exe -User Everyone
```

这个示例会报告，在由 C:\Policy.xml 指定的策略下，是否允许所有用户运行 calc.exe 而不允许运行 notepad.exe。

### 示例 2：未指定任何策略的可执行文件列表
```
PS C:\> Get-ChildItem C:\windows\system32\*.exe | Test-AppLockerPolicy c:\Policy.xml -Filter DeniedByDefault
```

这个例子列出了位于 C:\Windows\System32 目录下的可执行文件。根据 C:\Policy.xml 中指定的策略，所有用户都将无法访问这些文件，因为该策略中没有针对这些文件的明确允许或禁止规则。

### 示例 3：将没有指定策略的可执行文件列表写入文本文件
```
PS C:\> Get-AppLockerPolicy -Local | Test-AppLockerPolicy -Path C:\Windows\System32\*.exe -User contoso\saradavis -Filter Denied | Format-List -Property | Set-Content (ꞌC:\temp\DeniedFiles.txtꞌ)
```

这个示例获取本地的 AppLocker 策略，利用该策略来确定在 C:\Windows\System32 目录下哪些可执行文件被明确拒绝 contoso\saradavis 的访问权限（即这些文件无法被 saradavis 运行），然后将生成的列表内容重定向到一个文本文件中。

### 示例 4：列出软件包并根据策略进行测试
```
PS C:\> Get-AppxPackage -AllUsers | Test-AppLockerPolicy -XmlPolicy .\SamplePolicy.xml
```

这个示例列出了这台计算机上所有用户安装的所有软件包，并将这些软件包与保存的策略进行对比检查。

## 参数

### -Filter
指定用于过滤每个输入文件输出内容的策略决策。该参数的可接受值包括：Allowed（允许）、Denied（拒绝）、DeniedByDefault（默认拒绝）或AllowedByDefault（默认允许）。

```yaml
Type: System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.PolicyDecision]
Parameter Sets: (All)
Aliases:
Accepted values: Allowed, AllowedByDefault, Denied, DeniedByDefault

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Packages
指定一个已安装的应用程序列表，文件信息就是从这个列表中获取的。

```yaml
Type: System.Collections.Generic.List`1[Microsoft.Windows.Appx.PackageManager.Commands.AppxPackage]
Parameter Sets: ByXmlPolicyAppx
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Path
指定用于测试的文件路径列表。支持使用正则表达式。

```yaml
Type: System.Collections.Generic.List`1[System.String]
Parameter Sets: ByXmlPolicy, ByPolicyObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PolicyObject
指定 Applocker 策略。该策略可以通过 Get-AppLockerPolicy 或 New-AppLockerPolicy cmdlet 获取。

```yaml
Type: AppLockerPolicy
Parameter Sets: ByPolicyObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -User
用于指定AppLocker策略中规则测试的用户或组。该参数的可接受值包括：

- DNS user name (`domain\username`)
- User Principal Name (`username@domain.com`)
- SAM user name (`username`)
- Security identifier (`S-1-5-21-3165297888-301567370-576410423-1103`)

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

### -XmlPolicy
指定包含 AppLocker 策略的 XML 格式文件的路径和名称。

```yaml
Type: String
Parameter Sets: ByXmlPolicy, ByXmlPolicyAppx
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft SECURITY.ApplicationId.PolicyManagement.PolicyModel.AppLockerPolicy
**AppLockerPolicy**

## 输出

### Microsoft SECURITY.ApplicationId.PolicyManagement.AppLockerPolicyDecision

## 备注

## 相关链接

[Get-AppLockerFileInformation](./Get-AppLockerFileInformation.md)

[Get-AppLockerPolicy](./Get-AppLockerPolicy.md)

[新应用锁定策略](./New-AppLockerPolicy.md)

[Set-AppLockerPolicy](./Set-AppLockerPolicy.md)

